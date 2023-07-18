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
SUBMENU_SPACING = 75  # Increase the vertical spacing between submenu buttons


class Button:
    def __init__(self, x, y, width, height, text, font, action=None):
        self.text = text
        self.font = font
        self.action = action

        text_lines = text.split("\n")
        text_width = max(font.size(line)[0] for line in text_lines)
        text_height = font.size(text_lines[0])[1] * len(text_lines)
        self.width = max(
            width, text_width + 20
        )  # Add some padding to the button's width
        self.height = max(
            height, text_height + 20
        )  # Add some padding to the button's height

        self.rect = pygame.Rect(
            x - self.width // 2, y - self.height // 2, self.width, self.height
        )

    def draw(self, win, selected=False):
        button_color = BUTTON_SELECTED_COLOR if selected else BUTTON_COLOR
        pygame.draw.rect(win, button_color, self.rect)
        pygame.draw.rect(win, BLACK_COLOR, self.rect, 3)

        text_lines = self.text.split("\n")
        for i, line in enumerate(text_lines):
            text_surface = self.font.render(line, True, BLACK_COLOR)
            text_rect = text_surface.get_rect(
                centerx=self.rect.centerx,
                centery=self.rect.centery + (i * 20) - (len(text_lines) - 1) * 10,
            )
            win.blit(text_surface, text_rect)

    def check_collision(self, pos):
        return self.rect.collidepoint(pos)


class Menu:
    def __init__(self):
        self.win = self.initialize_pygame()
        self.menu_font = pygame.font.SysFont(None, 36)
        self.menu_items = ["Start Game", "Credit", "Exit"]
        self.submenu_items = [
            "Multi-player\n(Play with Friend)",
            "Single-player\n(Play with AI)",
            "Return to Main Menu",  # Add "Return to Main Menu" option
        ]
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
        num_submenu_items = len(self.submenu_items)
        submenu_height = num_submenu_items * SUBMENU_SPACING
        submenu_top_margin = (HEIGHT - submenu_height) // 2

        for i, item in enumerate(self.submenu_items):
            button_y = submenu_top_margin + i * SUBMENU_SPACING
            button = Button(
                WIDTH // 2, button_y, 200, 30, item, self.menu_font
            )  # Adjust height to 30
            buttons.append(button)
            button.draw(self.win)

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
                            if button.text == "Multi-player\n(Play with Friend)":
                                othello_gui = OthelloGUI()
                                othello_gui.run_game()

                            elif button.text == "Single-player\n(Play with AI)":
                                run_game()

                            elif button.text == "Return to Main Menu":
                                self.draw_menu()  # Go back to the main menu

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
