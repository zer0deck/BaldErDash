import os

import pygame

from ..importer import import_folder
from ..settings import SPEED

__all__ = ["Animation"]


class Animation(pygame.sprite.Sprite):
    def __init__(self, pos, groups, animations, type, status, size=0.5):
        super().__init__(groups)
        # animation
        self.animations = animations
        self.type = type
        self.assets(size)
        self.frame_index = 0
        self.animation_speed = 0.3
        self.status = status
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.damagebox = self.rect.inflate(-80, -60)

        # character status
        self.facing = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        self.dead = False

        # movement params
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = SPEED

    def assets(self, size):
        c_path = f"src/Assets/Sprites/{self.type[0]}/{self.type[1]}/"

        for animation in self.animations:
            path = c_path + animation
            self.animations[animation] = import_folder(path, size)

    def animate(self, status):
        animation = self.animations[status]
        if self.status == "die":
            self.dead = True
        self.frame_index += self.animation_speed

        if self.frame_index > len(animation):
            if self.dead:
                self.kill()
            self.frame_index = 0

        if self.facing:
            self.image = animation[int(self.frame_index)]
        else:
            self.image = pygame.transform.flip(
                animation[int(self.frame_index)], True, False
            )

        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

        self.damagebox.center = self.rect.center

    def shift(self, shift_speed):
        self.rect.x += shift_speed
