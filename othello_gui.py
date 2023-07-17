import pygame
import sys
from othello_game import OthelloGame

# Constants and colors
WIDTH, HEIGHT = 480, 480
BOARD_SIZE = 8
SQUARE_SIZE = HEIGHT // BOARD_SIZE
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (0, 128, 0)


class OthelloGUI:
    def __init__(self):
        self.win = self.initialize_pygame()
        self.game = OthelloGame()

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
                self.game.make_move(row, col)

    def run_game(self):
        while not self.game.is_game_over():
            self.handle_input()
            self.draw_board()

        pygame.quit()
        sys.exit()


def run_game():
    othello_gui = OthelloGUI()
    othello_gui.run_game()
