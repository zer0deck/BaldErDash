from decimal import ROUND_DOWN
import pygame
from settings import SPEED, TILESIZE
from importer import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # set animation
        self.assets()
        self.frame_index = 0
        # ! don't do animation speed aliquot to 1
        self.animation_speed = 0.3
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.facing = True

        # movement params
        self.direction = pygame.math.Vector2(0,0)
        self.speed = SPEED
        self.gravity_v = SPEED/10
        self.jump_speed = -SPEED*2

    def assets(self):
        c_path = '/Users/zer0deck/Documents/Документы/Git/BaldErDash/src/Assets/Sprites/Main_Character/Player/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'roll': [], 'climb': [], 'die':[], 'fall': []}

        for animation in self.animations:
            path = c_path + animation
            self.animations[animation] = import_folder(path)

    def animate(self, status):
        animation = self.animations[status]
        self.frame_index += self.animation_speed

        if self.frame_index > len(animation):
            self.frame_index = 0
        
        if self.facing:
            self.image = animation[int(self.frame_index)]
        else:
            self.image = pygame.transform.flip(animation[int(self.frame_index)], True, False)

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys [pygame.K_d]:
            self.direction.x = 1
            self.facing = True
        elif keys[pygame.K_LEFT] or keys [pygame.K_a]:
            self.direction.x = -1
            self.facing = False
        else:
            self.direction.x = 0
        
        if keys[pygame.K_SPACE]:
            self.jump()
    
    def gravity(self):
        self.direction.y  += self.gravity_v
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.get_status()
        self.animate(self.status)

