import pygame
import sys
from othello_gui import OthelloGUI, run_game

# Constants and colors
WIDTH, HEIGHT = 480, 320
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (0, 128, 0)
BUTTON_COLOR = (120, 120, 120)
BUTTON_SELECTED_COLOR = (200, 200, 200)


class Button:
    def __init__(self, x, y, width, height, text, font, action=None):
        self.text = text
        self.font = font
        self.action = action

        # Set the button's size based on the text's size
        text_surface = font.render(text, True, BLACK_COLOR)
        text_width, text_height = text_surface.get_size()
        self.width = max(
            width, text_width + 20
        )  # Add some padding to the button's width
        self.height = max(
            height, text_height + 10
        )  # Add some padding to the button's height

        # Center the button on the screen
        self.rect = pygame.Rect(
            x - self.width // 2, y - self.height // 2, self.width, self.height
        )

    def draw(self, win, selected=False):
        button_color = BUTTON_SELECTED_COLOR if selected else BUTTON_COLOR
        pygame.draw.rect(win, button_color, self.rect)
        pygame.draw.rect(win, BLACK_COLOR, self.rect, 3)

        text_surface = self.font.render(self.text, True, BLACK_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        win.blit(text_surface, text_rect)

    def check_collision(self, pos):
        return self.rect.collidepoint(pos)


class Menu:
    def __init__(self):
        self.win = self.initialize_pygame()
        self.menu_font = pygame.font.SysFont(None, 36)
        self.menu_items = ["Start Game", "Credit", "Exit"]
        self.submenu_items = ["Play with Friend", "Play with AI"]
        self.return_button = None

    def initialize_pygame(self):
        pygame.init()
        win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Othello - Main Menu")
        return win

    def draw_menu(self):
        self.win.fill(GREEN_COLOR)

        buttons = []
        for i, item in enumerate(self.menu_items):
            button = Button(
                WIDTH // 2, HEIGHT // 2 + i * 50, 200, 40, item, self.menu_font
            )
            buttons.append(button)
            button.draw(self.win)

        pygame.display.update()
        self.handle_input_menu(buttons)

    def draw_submenu(self):
        self.win.fill(GREEN_COLOR)

        buttons = []
        for i, item in enumerate(self.submenu_items):
            button = Button(
                WIDTH // 2, HEIGHT // 2 + i * 50, 200, 40, item, self.menu_font
            )
            buttons.append(button)
            button.draw(self.win)

        self.return_button = Button(
            WIDTH // 2,
            HEIGHT // 2 + len(self.submenu_items) * 50 + 30,
            200,
            40,
            "Return to Main Menu",
            self.menu_font,
            self.draw_menu,
        )
        self.return_button.draw(self.win)

        pygame.display.update()
        self.handle_input_submenu(buttons)

    def draw_credit(self):
        self.win.fill(GREEN_COLOR)

        credit_text = "Written and Developed by AmirHossein Roodaki"
        github_link = "GitHub: /Roodaki"
        return_button_text = "Return to Main Menu"

        credit_surface = self.menu_font.render(credit_text, True, BLACK_COLOR)
        github_surface = self.menu_font.render(github_link, True, BLACK_COLOR)

        credit_rect = credit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        github_rect = github_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        self.return_button = Button(
            WIDTH // 2,
            HEIGHT // 2 + 40,
            200,
            40,
            return_button_text,
            self.menu_font,
            self.draw_menu,
        )
        self.return_button.draw(self.win)

        self.win.blit(credit_surface, credit_rect)
        self.win.blit(github_surface, github_rect)

        pygame.display.update()
        self.handle_input_credit()

    def handle_input_menu(self, buttons):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for button in buttons:
                        if button.check_collision((x, y)):
                            if button.text == "Start Game":
                                self.draw_submenu()
                            elif button.text == "Credit":
                                self.draw_credit()
                            elif button.text == "Exit":
                                pygame.quit()
                                sys.exit()

    def handle_input_submenu(self, buttons):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for button in buttons:
                        if button.check_collision((x, y)):
                            if button.text == "Play with Friend":
                                othello_gui = OthelloGUI()
                                othello_gui.run_game()

                            elif button.text == "Play with AI":
                                run_game()

                    if self.return_button.check_collision(
                        (x, y)
                    ):  # Handle the return button
                        self.draw_menu()

    def handle_input_credit(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.return_button.check_collision((x, y)):
                        self.perform_action(self.return_button.action)

    def perform_action(self, action):
        if action is None:
            pygame.quit()
            sys.exit()
        else:
            action()


def run_menu():
    menu = Menu()
    menu.draw_menu()
