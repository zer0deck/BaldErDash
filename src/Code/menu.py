import pygame

from .settings import UI_FONT, UI_FONT_SIZE

__all__ = ["main_Menu", "iteration_Menu"]


class main_Menu(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("src/Assets/GUI/Panels/panel_2.png")
        self.image = pygame.transform.smoothscale(
            self.image, (self.image.get_width() * 0.8, self.image.get_height() * 0.8)
        )
        self.pos = (
            (self.display_surface.get_width() - self.image.get_width()) // 2,
            (self.display_surface.get_height() - self.image.get_height()) // 2,
        )
        self.rect = self.image.get_rect(topleft=self.pos)


class iteration_Menu(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("src/Assets/GUI/Panels/panel_1.png")
        self.pos = (
            (self.display_surface.get_width() - self.image.get_width()) // 2,
            (self.display_surface.get_height() - self.image.get_height()) // 2,
        )
        self.rect = self.image.get_rect(topleft=self.pos)

    def add_text(self, text):
        self.text = self.font.render(text, True, (0, 0, 0))

    def draw_text(self):
        self.image.blit(
            self.text,
            (20, 20),
        )

        self.image.blit(
            self.font.render("Press I to exit.", True, (0, 0, 0)),
            (self.image.get_width() // 5 * 2, self.image.get_height() // 10 * 9),
        )
