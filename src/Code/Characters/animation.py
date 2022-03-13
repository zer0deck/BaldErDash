import pygame
from Code.importer import import_folder
from Code.settings import SPEED

class Animation(pygame.sprite.Sprite):
    def __init__(self, pos, groups, animations, type, status, size = 1):
        super().__init__(groups)
        # animation 
        self.animations = animations
        self.type = type
        self.assets(size)
        self.frame_index = 0
        self.animation_speed = 0.3
        self.status = status
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # character status
        self.facing = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        # movement params
        self.direction = pygame.math.Vector2(0,0)
        self.speed = SPEED

    def assets(self, size):
        c_path = f'src/Assets/Sprites/{self.type[0]}/{self.type[1]}/'

        for animation in self.animations:
            path = c_path + animation
            self.animations[animation] = import_folder(path, size)
    
    def animate(self, status):
        animation = self.animations[status]
        self.frame_index += self.animation_speed

        if self.frame_index > len(animation):
            self.frame_index = 0
        
        if self.facing:
            self.image = animation[int(self.frame_index)]
        else:
            self.image = pygame.transform.flip(animation[int(self.frame_index)], True, False)
        
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
    
    def shift(self, shift_speed):
        self.rect.x += shift_speed