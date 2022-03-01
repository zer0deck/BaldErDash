import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, map, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'src/Assets/Enviroments/Tilesets/{map}/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)