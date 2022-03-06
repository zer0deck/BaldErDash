import pygame
from settings import SPEED


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('src/Assets/Sprites/Main_Character/Player/run/player_run_00.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        # movement params
        self.direction = pygame.math.Vector2(0,0)
        self.speed = SPEED
        self.gravity_v = SPEED/10
        self.jump_speed = -SPEED*2

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

