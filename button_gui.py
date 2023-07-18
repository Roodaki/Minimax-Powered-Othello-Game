import pygame

BUTTON_COLOR = (120, 120, 120)
BUTTON_SELECTED_COLOR = (200, 200, 200)


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
        pygame.draw.rect(win, pygame.Color("black"), self.rect, 3)

        text_lines = self.text.split("\n")
        for i, line in enumerate(text_lines):
            text_surface = self.font.render(line, True, pygame.Color("black"))
            text_rect = text_surface.get_rect(
                centerx=self.rect.centerx,
                centery=self.rect.centery + (i * 20) - (len(text_lines) - 1) * 10,
            )
            win.blit(text_surface, text_rect)

    def check_collision(self, pos):
        return self.rect.collidepoint(pos)
