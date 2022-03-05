import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)

    def shift(self, shift_speed):
        self.rect.x += shift_speed

    def update(self, speed):
        self.shift(speed)
    

# class Floor(Objectmove):
#     def __init__(self, map, pos, groups):
#         super().__init__(groups)


# class Wall(Objectmove):
#     def __init__(self, map, pos, groups):
#         super().__init__(groups)
#         self.image = pygame.image.load(f'src/Assets/Tilesets/Forest/image_part_003.png').convert_alpha()
#         self.rect = self.image.get_rect(topleft = pos)
    

# class Entrance(Objectmove):
#     def __init__(self, map, pos, groups):
#         super().__init__(groups)
#         self.image = pygame.image.load(f'src/Assets/Tilesets/Forest/image_part_003.png').convert_alpha()
#         self.rect = self.image.get_rect(topleft = pos)


# class Ladder(Objectmove):
#     def __init__(self, map, pos, groups):
#         super().__init__(groups)
#         self.image = pygame.image.load(f'src/Assets/Tilesets/Forest/image_part_003.png').convert_alpha()
#         self.rect = self.image.get_rect(topleft = pos)
