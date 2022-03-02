import pygame
from settings import TILESIZE, SPEED, GRAVITY, map
from background import Background
from objects import Wall
from player import Player
from debug import debug

class Level:
    def __init__(self, surface, mapname, screen):
        
        self.display_surface = surface
        self.world_shift = [0,0]
        self.player = pygame.sprite.GroupSingle()
        self.player_group = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.background = Background(mapname=mapname, screen=screen)
        self.create_map(mapname)

    def create_map(self, mapname):
        for i, row in enumerate(map(mapname)):
            for j, col in enumerate(row):
                x = j * TILESIZE
                y = i * TILESIZE
                if col == 'x':
                    Wall(mapname, (x,y),[self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.psprite = Player((x,y), self.obstacle_sprites, SPEED, GRAVITY)
                    self.player.add(self.psprite)

    def scroll(self):
        player = self.player.sprite
        x_pos = player.rect.centerx
        y_pos = player.rect.centery
        x_dir = player.direction.x
        y_dir = player.direction.y
        
        if y_pos < 250 and y_dir < 0:
            self.world_shift[1] = SPEED
            player.speed = 0
        elif y_pos > 500 and y_dir > 0:
            self.world_shift[1] = -SPEED
            player.speed = 0
        else:
            self.world_shift[1] = 0
            player.speed = SPEED

        if x_pos < 150 and x_dir < 0:
            self.world_shift[0] = SPEED
            player.speed = 0
        elif x_pos > 1130 and x_dir > 0:
            self.world_shift[0] = -SPEED
            player.speed = 0
        else:
            self.world_shift[0] = 0
            player.speed = SPEED


    def launch(self):
        self.background.update(self.world_shift[0])
        self.player.draw(self.display_surface)
        self.player.update()
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update(self.world_shift)
        self.scroll()
        debug(self.psprite.direction)


