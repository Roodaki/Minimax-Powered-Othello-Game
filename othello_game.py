class OthelloGame:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 1
        self.board[3][4] = -1
        self.board[4][3] = -1
        self.board[4][4] = 1
        self.current_player = 1

    def is_valid_move(self, row, col):
        """
        Check if the move is valid and results in flipping opponent disks.
        """
        if self.board[row][col] != 0:
            return False

        # Check in all eight directions for opponent disks to flip
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while (
                0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == -self.current_player
            ):
                r += dr
                c += dc
                if (
                    0 <= r < 8
                    and 0 <= c < 8
                    and self.board[r][c] == self.current_player
                ):
                    return True

        return False

    def flip_disks(self, row, col):
        """
        Flip the opponent's disks after placing a disk at the given position.
        """
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            flip_list = []
            while (
                0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == -self.current_player
            ):
                flip_list.append((r, c))
                r += dr
                c += dc
                if (
                    0 <= r < 8
                    and 0 <= c < 8
                    and self.board[r][c] == self.current_player
                ):
                    for fr, fc in flip_list:
                        self.board[fr][fc] = self.current_player

    def make_move(self, row, col):
        """
        Make a move at the given position for the current player if it's a valid move.
        """
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.flip_disks(row, col)
            self.current_player *= -1

    def is_game_over(self):
        """
        Check if the game is over (no more valid moves or board is full).
        """
        return not self.get_valid_moves() or all(
            all(cell != 0 for cell in row) for row in self.board
        )

    def get_winner(self):
        """
        Get the winner of the game (1 for Black, -1 for White, 0 for a tie).
        """
        black_count = sum(row.count(1) for row in self.board)
        white_count = sum(row.count(-1) for row in self.board)

        if black_count > white_count:
            return 1
        elif black_count < white_count:
            return -1
        else:
            return 0

    def get_valid_moves(self):
        """
        Get a list of valid moves for the current player.
        """
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves
