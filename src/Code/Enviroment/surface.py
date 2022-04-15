import pygame

__all__ = ["Tile"]
# This is the initializer for tiles
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def shift(self, shift_speed):
        self.rect.x += shift_speed

    def update(self, speed):
        self.shift(speed)
