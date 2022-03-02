import pygame

class Floor(pygame.sprite.Sprite):
    def __init__(self, map, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'src/Assets/Enviroments/Tilesets/{map}/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def shift(self, shift_speed):
        self.rect.x += shift_speed

    def update(self, speed):
        self.shift(speed)

class Wall(pygame.sprite.Sprite):
    def __init__(self, map, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'src/Assets/Enviroments/Tilesets/{map}/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    
    def shift(self, shift_speed):
        self.rect.x += shift_speed

    def update(self, speed):
        self.shift(speed)

class Entrance(pygame.sprite.Sprite):
    def __init__(self, map, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'src/Assets/Enviroments/Tilesets/{map}/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def shift(self, shift_speed):
        self.rect.x += shift_speed

    def update(self, speed):
        self.shift(speed)

class Ladder(pygame.sprite.Sprite):
    def __init__(self, map, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'src/Assets/Enviroments/Tilesets/{map}/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def shift(self, shift_speed):
        self.rect.x += shift_speed

    def update(self, speed):
        self.shift(speed)