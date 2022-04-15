import pygame

from .settings import ENERGY, HEALTH, HEIGHT, UI_FONT, UI_FONT_SIZE, WIDTH

__all__ = ["UI"]


class UI:
    def __init__(self):
        self.uigroup = pygame.sprite.Group()
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # health bar setup
        self.temp_health = HEALTH
        self.health_bar_bg = UIobject(
            (134, 34),
            self.uigroup,
            "src/Assets/GUI/Stats/character_hp_bar_bg.png",
        )
        self.health_bar_fill = UIobject(
            (134, 34),
            self.uigroup,
            "src/Assets/GUI/Stats/character_hp_bar_fill.png",
            [
                self.health_bar_bg.image.get_width(),
                self.health_bar_bg.image.get_height(),
            ],
        )
        self.health_bar_frame = UIobject(
            (130, 30),
            self.uigroup,
            "src/Assets/GUI/Stats/character_hp_bar_frame.png",
        )

        # energy bar setup
        self.temp_energy = ENERGY
        self.energy_bar_bg = UIobject(
            (134, 94), self.uigroup, "src/Assets/GUI/Stats/character_energy_bar_bg.png"
        )
        self.energy_bar_fill = UIobject(
            (134, 94),
            self.uigroup,
            "src/Assets/GUI/Stats/character_energy_bar_fill.png",
            [
                self.energy_bar_bg.image.get_width(),
                self.energy_bar_bg.image.get_height(),
            ],
        )
        self.energy_bar_frame = UIobject(
            (130, 90),
            self.uigroup,
            "src/Assets/GUI/Stats/character_energy_bar_frame.png",
        )

        # player logo setup
        self.temp_exp = 0
        self.portrait = UIobject(
            (20, 10), self.uigroup, "src/Assets/GUI/Stats/portrait.png"
        )
        self.player_exp = UIobject(
            (10, 110), self.uigroup, "src/Assets/GUI/Stats/character_xp_bar.png"
        )
        self.player_portrait = UIobject(
            (
                (
                    self.portrait.image.get_width()
                    - pygame.image.load(
                        "src/Assets/GUI/Stats/portrait_character.png"
                    ).get_width()
                )
                + 20,
                (
                    self.portrait.image.get_height()
                    - pygame.image.load(
                        "src/Assets/GUI/Stats/portrait_character.png"
                    ).get_height()
                )
                + 10,
            ),
            self.uigroup,
            "src/Assets/GUI/Stats/portrait_character.png",
        )

    def update(self, player):
        if player.health < self.temp_health and player.health > 0:
            self.health_bar_fill.image = pygame.transform.scale(
                self.health_bar_fill.image,
                (
                    self.health_bar_bg.image.get_width() * player.health / HEALTH,
                    self.health_bar_bg.image.get_height(),
                ),
            )
            self.temp_health = player.health

        if player.energy < self.temp_energy and player.energy > 0:
            self.energy_bar_fill.image = pygame.transform.scale(
                self.energy_bar_fill.image,
                (
                    self.energy_bar_bg.image.get_width() * player.energy / ENERGY,
                    self.energy_bar_bg.image.get_height(),
                ),
            )
            self.temp_energy = player.energy

        # if player.exp > self.temp_exp:

    def display(self, player):
        self.update(player)
        self.uigroup.draw(self.display_surface)


class UIobject(pygame.sprite.Sprite):
    def __init__(
        self, pos, group, path: str, scale: list = None, transparancy: int = None
    ):
        super().__init__(group)
        self.scale = scale
        if self.scale:
            self.image = pygame.transform.smoothscale(
                pygame.image.load(path), (self.scale[0], self.scale[1])
            )
        else:
            self.image = pygame.image.load(path)
            self.image = pygame.transform.smoothscale(
                self.image,
                (
                    round(self.image.get_width() * WIDTH / 1536),
                    round(self.image.get_height() * HEIGHT / 864),
                ),
            )

        if transparancy:
            self.image.fill(
                (255, 255, 255, 2.55 * transparancy), None, pygame.BLEND_RGBA_MULT
            )

        self.rect = self.image.get_rect(topleft=pos)
