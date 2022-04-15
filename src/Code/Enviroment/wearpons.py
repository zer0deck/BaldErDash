import pygame

__all__ = ["Wearpon"]


class Wearpon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.facing = player.facing
        # graphic
        self.image = pygame.Surface((40, 40))  # pygame.SRCALPHA

        # placement
        if player.type == "Player Sword":
            if player.facing:
                self.rect = self.image.get_rect(midright=player.rect.midright)
            else:
                self.rect = self.image.get_rect(midleft=player.rect.midleft)
