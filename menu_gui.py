import pygame
import sys
from othello_gui import OthelloGUI, run_game
from button_gui import Button

# Constants and colors
WIDTH, HEIGHT = 480, 320
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (0, 128, 0)
SUBMENU_SPACING = 75  # Increase the vertical spacing between submenu buttons


class Menu:
    def __init__(self):
        """
        A class representing the main menu of the Othello game.

        Attributes:
            win (pygame.Surface): The Pygame window.
            menu_font (pygame.font.Font): The font used for rendering the menu items.
            menu_items (list): The list of menu items displayed on the main menu.
            submenu_items (list): The list of submenu items displayed after selecting "Start Game".
            return_button (Button): The button to return to the main menu from the credit screen.
        """
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
        """
        Initialize Pygame and create a window for the main menu.

        Returns:
            pygame.Surface: The Pygame window.
        """
        pygame.init()
        win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Othello - Main Menu")
        return win

    def draw_menu(self):
        """
        Draw the main menu on the Pygame window.
        """
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
        """
        Draw the submenu on the Pygame window.
        """
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
        """
        Draw the credit screen on the Pygame window.
        """
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
        """
        Handle input events for the main menu.

        Parameters:
            buttons (list): The list of buttons in the main menu.
        """
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
        """
        Handle input events for the submenu.

        Parameters:
            buttons (list): The list of buttons in the submenu.
        """
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
                                self.run_single_player_game()

                            elif button.text == "Return to Main Menu":
                                self.draw_menu()  # Go back to the main menu

    def run_single_player_game(self):
        """
        Start a single-player game with AI.
        """
        # Pass "ai" as the player_mode to indicate the single-player mode with AI
        othello_gui = OthelloGUI(player_mode="ai")
        othello_gui.run_game()

    def handle_input_credit(self):
        """
        Handle input events for the credit screen.
        """
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
        """
        Perform the specified action.

        Parameters:
            action (callable): The function to be called as the action.
        """
        if action is None:
            pygame.quit()
            sys.exit()
        else:
            action()


def run_menu():
    """
    Start the main menu of the Othello game.
    """
    menu = Menu()
    menu.draw_menu()
