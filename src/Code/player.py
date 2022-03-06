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
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # movement params
        self.direction = pygame.math.Vector2(0,0)
        self.speed = SPEED
        self.gravity_v = SPEED/10
        self.jump_speed = -SPEED*2

    def assets(self):
        c_path = '/Users/zer0deck/Documents/Документы/Git/BaldErDash/src/Assets/Sprites/Main_Character/Player/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'roll': [], 'climb': [], 'die':[]}

        for animation in self.animations:
            path = c_path + animation
            self.animations[animation] = import_folder(path)

    def animate(self):
        animation = self.animations['idle']
        self.frame_index += self.animation_speed

        if self.frame_index > len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys [pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys [pygame.K_a]:
            self.direction.x = -1
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
        self.animate()

