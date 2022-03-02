import pygame
from settings import MAP, TILESIZE, SPEED
from objects import Wall
from player import Player

class Level:
    def __init__(self, surface, mapname):
        
        self.display_surface = surface
        self.world_shift = 0
        self.player = pygame.sprite.GroupSingle()
        self.player_group = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map(mapname)

    def create_map(self, mapname):
        for i, row in enumerate(MAP[mapname]):
            for j, col in enumerate(row):
                x = j * TILESIZE
                y = i * TILESIZE
                if col == 'x':
                    Wall(mapname, (x,y),[self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    psprite = Player((x,y), self.obstacle_sprites, SPEED)
                    self.player.add(psprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < 20 and direction_x < 0:
            self.world_shift = SPEED
            player.speed = 0
        elif player_x > 1960 and direction_x > 0:
            self.world_shift = -SPEED
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = SPEED


    def launch(self):
        self.player.draw(self.display_surface)
        self.player.update()
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update(self.world_shift)
        self.scroll_x()



