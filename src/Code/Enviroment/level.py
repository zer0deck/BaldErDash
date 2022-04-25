# -*- coding: utf-8 -*-

import pygame

from ..debug import debug
from ..settings import DASH_POWER, HEIGHT, JUMPS, SPEED, WIDTH
from ..ui import UI
from .background import Background
from .map import Map
from .wearpons import Wearpon

__all__ = ["Level"]


class Level:
    def __init__(self, surface, mapname):

        # init screen
        self.display_surface = surface
        self.background = Background(mapname=mapname, screen=self.display_surface)

        # collisions
        self.current_attack = None
        self.current_x = 0
        self.world_shift = 0

        # init sprites groups
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.damageboxes = pygame.sprite.Group()

        # UI
        self.ui = UI()

        # map creation
        self.create_level(mapname)

    def create_level(self, mapname):
        fmap = Map(mapname)
        player = fmap.create(
            tile_groups=[self.visible_sprites, self.obstacle_sprites],
            enemy_groups=[self.visible_sprites, self.enemies],
            player_attack=[self.player_attack, self.destroy_attack],
        )
        self.player.add(player)

    def scroll(self):

        player = self.player.sprite
        x_pos = player.rect.centerx
        x_dir = player.direction.x
        if player.dashing:
            inertia = SPEED * DASH_POWER
        else:
            inertia = SPEED

        if x_pos < WIDTH * 0.4 and x_dir < 0:
            self.world_shift = inertia
            player.speed = 0

        elif x_pos > WIDTH * 0.6 and x_dir > 0:
            self.world_shift = -inertia
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = SPEED

    def collision(self, direct):
        player = self.player.sprite

        if direct == "h":
            player.rect.x += player.direction.x * player.speed

            # horizontal coll
            for sprite in self.obstacle_sprites.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                        player.on_left = True
                        self.current_x = player.rect.left
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left
                        player.on_right = True
                        self.current_x = player.rect.right

            if player.on_left and (
                player.rect.left < self.current_x or (player.direction.x >= 0)
            ):
                player.on_left = False
            if player.on_right and (
                player.rect.right < self.current_x or (player.direction.x >= 0)
            ):
                player.on_right = False

            for sprite in self.enemies.sprites():
                if sprite.damagebox.colliderect(player.hitbox):
                    player.health -= 1
                if self.current_attack:
                    if self.current_attack.rect.colliderect(sprite.rect):
                        sprite.health -= player.wearpon[player.attack_type]["damage"]

        elif direct == "v":
            player.gravity()

            # vertical coll
            for sprite in self.obstacle_sprites.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                        player.on_ground = True
                        player.can_jump = JUMPS
                    elif player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0
                        player.on_ceiling = True

            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False

        else:
            print("crash")

    def player_attack(self):
        self.current_attack = Wearpon(
            self.player.sprite, [self.visible_sprites, self.damageboxes]
        )

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def show_hitboxes(self):
        pygame.draw.rect(
            self.display_surface,
            color=(1, 1, 255),
            rect=self.player.sprite.rect,
        )
        pygame.draw.rect(
            self.display_surface,
            color=(1, 255, 1),
            rect=self.player.sprite.hitbox,
        )
        for sprite in self.enemies.sprites():
            pygame.draw.rect(
                self.display_surface,
                color=(255, 1, 1),
                rect=sprite.damagebox,
            )

    def launch(self, debug_v=True):

        # background movement
        self.background.update(self.world_shift)

        # player movement
        self.show_hitboxes()
        self.player.draw(self.display_surface)
        self.player.update()
        self.collision("h")
        self.collision("v")

        # surface movement
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update(self.world_shift)

        # enemies

        self.scroll()
        self.ui.display(self.player.sprite)

        # debug
        if debug_v == True:
            debug(self.player.sprite.direction)
