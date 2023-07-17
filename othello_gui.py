import pygame
import sys
from othello_game import OthelloGame

# Constants and colors
WIDTH, HEIGHT = 480, 560  # Increase the height to accommodate the messaging area
BOARD_SIZE = 8
SQUARE_SIZE = (HEIGHT - 80) // BOARD_SIZE  # Adjust SQUARE_SIZE to fit messaging area
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (0, 128, 0)


class OthelloGUI:
    def __init__(self):
        self.win = self.initialize_pygame()
        self.game = OthelloGame()
        self.message_font = pygame.font.SysFont(None, 24)
        self.message = ""

    def initialize_pygame(self):
        pygame.init()
        win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Othello")
        return win

    def draw_board(self):
        self.win.fill(GREEN_COLOR)

        # Draw board grid
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                pygame.draw.rect(
                    self.win,
                    BLACK_COLOR,
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                    1,
                )
                if self.game.board[row][col] == 1:
                    pygame.draw.circle(
                        self.win,
                        BLACK_COLOR,
                        ((col + 0.5) * SQUARE_SIZE, (row + 0.5) * SQUARE_SIZE),
                        SQUARE_SIZE // 2 - 4,
                    )
                elif self.game.board[row][col] == -1:
                    pygame.draw.circle(
                        self.win,
                        WHITE_COLOR,
                        ((col + 0.5) * SQUARE_SIZE, (row + 0.5) * SQUARE_SIZE),
                        SQUARE_SIZE // 2 - 4,
                    )

        # Draw messaging area
        message_area_rect = pygame.Rect(
            0, BOARD_SIZE * SQUARE_SIZE, WIDTH, HEIGHT - (BOARD_SIZE * SQUARE_SIZE)
        )
        pygame.draw.rect(self.win, WHITE_COLOR, message_area_rect)

        # Draw player's turn message
        player_turn = "Black's" if self.game.current_player == 1 else "White's"
        turn_message = f"{player_turn} turn"
        message_surface = self.message_font.render(turn_message, True, BLACK_COLOR)
        message_rect = message_surface.get_rect(
            center=(WIDTH // 2, (HEIGHT + BOARD_SIZE * SQUARE_SIZE) // 2 - 20)
        )
        self.win.blit(message_surface, message_rect)

        # Draw invalid move message
        if self.message:
            invalid_move_message = self.message
            message_surface = self.message_font.render(
                invalid_move_message, True, BLACK_COLOR
            )
            message_rect = message_surface.get_rect(
                center=(WIDTH // 2, (HEIGHT + BOARD_SIZE * SQUARE_SIZE) // 2 + 20)
            )
            self.win.blit(message_surface, message_rect)

        pygame.display.update()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE
                if self.game.is_valid_move(row, col):
                    self.game.make_move(row, col)
                    self.message = ""  # Clear any previous messages
                else:
                    self.message = "Invalid move! Try again."

    def run_game(self):
        while not self.game.is_game_over():
            self.handle_input()
            self.draw_board()

        winner = self.game.get_winner()
        if winner == 1:
            self.message = "Black wins!"
        elif winner == -1:
            self.message = "White wins!"
        else:
            self.message = "It's a tie!"

        self.draw_board()
        pygame.time.delay(2000)  # Display the result for 2 seconds before quitting

        pygame.quit()
        sys.exit()


def run_game():
    othello_gui = OthelloGUI()
    othello_gui.run_game()
