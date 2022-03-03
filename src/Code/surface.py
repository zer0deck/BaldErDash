import pygame

class Objectmove(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

    def shift(self, shift_speed):
        self.rect.x += shift_speed

    def update(self, speed):
        self.shift(speed)
    

class Floor(Objectmove):
    def __init__(self, map, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'src/Assets/Enviroments/Tiles/{map}/Tile_01.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)


class Wall(Objectmove):
    def __init__(self, map, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'src/Assets/Enviroments/Tiles/{map}/Tile_01.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    

class Entrance(Objectmove):
    def __init__(self, map, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'src/Assets/Enviroments/Tiles/{map}/Tile_01.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)


class Ladder(Objectmove):
    def __init__(self, map, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'src/Assets/Enviroments/Tiles/{map}/Tile_01.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def shift(self, shift_speed):
        self.rect.x += shift_speed[0]
        self.rect.y += shift_speed[1]

    def update(self, speed):
        self.shift(speed)