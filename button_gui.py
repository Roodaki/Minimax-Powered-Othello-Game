import pygame

BUTTON_COLOR = (120, 120, 120)
BUTTON_SELECTED_COLOR = (200, 200, 200)


class Button:
    def __init__(self, x, y, width, height, text, font, action=None):
        """
        A class representing a button in a Pygame GUI.

        Parameters:
            x (int): The x-coordinate of the button's center.
            y (int): The y-coordinate of the button's center.
            width (int): The width of the button.
            height (int): The height of the button.
            text (str): The text to be displayed on the button.
            font (pygame.font.Font): The font used for rendering the text.
            action (callable, optional): The function to be called when the button is clicked. Defaults to None.

        Attributes:
            text (str): The text displayed on the button.
            font (pygame.font.Font): The font used for rendering the text.
            action (callable): The function to be called when the button is clicked.
            rect (pygame.Rect): The rectangle representing the button's position and size.
        """
        self.text = text
        self.font = font
        self.action = action

        # Split the text into lines and calculate the required button size based on the text content
        text_lines = text.split("\n")
        text_width = max(font.size(line)[0] for line in text_lines)
        text_height = font.size(text_lines[0])[1] * len(text_lines)
        self.width = max(
            width, text_width + 20
        )  # Add some padding to the button's width
        self.height = max(
            height, text_height + 20
        )  # Add some padding to the button's height

        # Create a rectangle representing the button's position and size
        self.rect = pygame.Rect(
            x - self.width // 2, y - self.height // 2, self.width, self.height
        )

    def draw(self, win, selected=False):
        """
        Draw the button on the Pygame window.

        Parameters:
            win (pygame.Surface): The Pygame window to draw the button on.
            selected (bool, optional): True if the button is selected, False otherwise. Defaults to False.
        """
        button_color = BUTTON_SELECTED_COLOR if selected else BUTTON_COLOR

        # Draw the button rectangle with the specified color and black border
        pygame.draw.rect(win, button_color, self.rect)
        pygame.draw.rect(win, pygame.Color("black"), self.rect, 3)

        # Split the text into lines and render each line on the button
        text_lines = self.text.split("\n")
        for i, line in enumerate(text_lines):
            text_surface = self.font.render(line, True, pygame.Color("black"))
            text_rect = text_surface.get_rect(
                centerx=self.rect.centerx,
                centery=self.rect.centery + (i * 20) - (len(text_lines) - 1) * 10,
            )
            win.blit(text_surface, text_rect)

    def check_collision(self, pos):
        """
        Check if a given position collides with the button.

        Parameters:
            pos (tuple): The (x, y) position to check collision with.

        Returns:
            bool: True if the position collides with the button, False otherwise.
        """
        return self.rect.collidepoint(pos)
