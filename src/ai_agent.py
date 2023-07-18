from othello_game import OthelloGame


def get_best_move(game, max_depth=8):
    """
    Given the current game state, this function returns the best move for the AI player using the Alpha-Beta Pruning
    algorithm with a specified maximum search depth.

    Parameters:
        game (OthelloGame): The current game state.
        max_depth (int): The maximum search depth for the Alpha-Beta algorithm.

    Returns:
        tuple: A tuple containing the evaluation value of the best move and the corresponding move (row, col).
    """
    _, best_move = alphabeta(game, max_depth)
    return best_move


def alphabeta(
    game, max_depth, maximizing_player=True, alpha=float("-inf"), beta=float("inf")
):
    """
    Alpha-Beta Pruning algorithm for selecting the best move for the AI player.

    Parameters:
        game (OthelloGame): The current game state.
        max_depth (int): The maximum search depth for the Alpha-Beta algorithm.
        maximizing_player (bool): True if maximizing player (AI), False if minimizing player (opponent).
        alpha (float): The alpha value for pruning. Defaults to negative infinity.
        beta (float): The beta value for pruning. Defaults to positive infinity.

    Returns:
        tuple: A tuple containing the evaluation value of the best move and the corresponding move (row, col).
    """
    if max_depth == 0 or game.is_game_over():
        return evaluate_game_state(game), None

    valid_moves = game.get_valid_moves()

    if maximizing_player:
        max_eval = float("-inf")
        best_move = None

        for move in valid_moves:
            new_game = OthelloGame(player_mode=game.player_mode)
            new_game.board = [row[:] for row in game.board]
            new_game.current_player = game.current_player
            new_game.make_move(*move)

            eval, _ = alphabeta(new_game, max_depth - 1, False, alpha, beta)

            if eval > max_eval:
                max_eval = eval
                best_move = move

            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval, best_move
    else:
        min_eval = float("inf")
        best_move = None

        for move in valid_moves:
            new_game = OthelloGame(player_mode=game.player_mode)
            new_game.board = [row[:] for row in game.board]
            new_game.current_player = game.current_player
            new_game.make_move(*move)

            eval, _ = alphabeta(new_game, max_depth - 1, True, alpha, beta)

            if eval < min_eval:
                min_eval = eval
                best_move = move

            beta = min(beta, eval)
            if beta <= alpha:
                break

        return min_eval, best_move


def evaluate_game_state(game):
    """
    Evaluates the current game state for the AI player.

    Parameters:
        game (OthelloGame): The current game state.

    Returns:
        float: The evaluation value representing the desirability of the game state for the AI player.
    """
    # Evaluation weights for different factors
    coin_parity_weight = 1.0
    mobility_weight = 2.0
    corner_occupancy_weight = 5.0
    stability_weight = 3.0
    edge_occupancy_weight = 2.5

    # Coin parity (difference in disk count)
    player_disk_count = sum(row.count(game.current_player) for row in game.board)
    opponent_disk_count = sum(row.count(-game.current_player) for row in game.board)
    coin_parity = player_disk_count - opponent_disk_count

    # Mobility (number of valid moves for the current player)
    player_valid_moves = len(game.get_valid_moves())
    opponent_valid_moves = len(
        OthelloGame(player_mode=-game.current_player).get_valid_moves()
    )
    mobility = player_valid_moves - opponent_valid_moves

    # Corner occupancy (number of player disks in the corners)
    corner_occupancy = sum(
        game.board[i][j] for i, j in [(0, 0), (0, 7), (7, 0), (7, 7)]
    )

    # Stability (number of stable disks)
    stability = calculate_stability(game)

    # Edge occupancy (number of player disks on the edges)
    edge_occupancy = sum(game.board[i][j] for i in [0, 7] for j in range(1, 7)) + sum(
        game.board[i][j] for i in range(1, 7) for j in [0, 7]
    )

    # Combine the factors with the corresponding weights to get the final evaluation value
    evaluation = (
        coin_parity * coin_parity_weight
        + mobility * mobility_weight
        + corner_occupancy * corner_occupancy_weight
        + stability * stability_weight
        + edge_occupancy * edge_occupancy_weight
    )

    return evaluation


def calculate_stability(game):
    """
    Calculates the stability of the AI player's disks on the board.

    Parameters:
        game (OthelloGame): The current game state.

    Returns:
        int: The number of stable disks for the AI player.
    """

    def neighbors(row, col):
        return [
            (row + dr, col + dc)
            for dr in [-1, 0, 1]
            for dc in [-1, 0, 1]
            if (dr, dc) != (0, 0) and 0 <= row + dr < 8 and 0 <= col + dc < 8
        ]

    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    edges = [(i, j) for i in [0, 7] for j in range(1, 7)] + [
        (i, j) for i in range(1, 7) for j in [0, 7]
    ]
    inner_region = [(i, j) for i in range(2, 6) for j in range(2, 6)]
    regions = [corners, edges, inner_region]

    stable_count = 0

    def is_stable_disk(row, col):
        return (
            all(game.board[r][c] == game.current_player for r, c in neighbors(row, col))
            or (row, col) in edges + corners
        )

    for region in regions:
        for row, col in region:
            if game.board[row][col] == game.current_player and is_stable_disk(row, col):
                stable_count += 1

    return stable_count
