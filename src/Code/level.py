import pygame
from settings import MAP, TILESIZE
from tile import Tile
from player import Player

class Level:
    def __init__(self) -> None:
        
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for i, row in enumerate(MAP):
            for j, col in enumerate(row):
                x = j * TILESIZE
                y = i * TILESIZE
                if col is 'x':
                    Tile('AW', (x,y),[self.visible_sprites, self.obstacle_sprites])
                if col is 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)
                    

    def launch(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()

