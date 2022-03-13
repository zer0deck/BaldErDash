import os, sys
import pygame
from Code.Enviroment.surface import Tile
from Code.Characters.player import Player
from Code.settings import TILESIZE
from Code.Characters.enemies import Bat

from Maps.Forest import forest

class Map():
    def __init__(self, mapname):
        pygame.init()
        self.images = []
        self. array = []
        if mapname == 'Forest':
            self.array, self.images = forest(TILESIZE)
        self.dic = {}
        for ind, image in enumerate(self.images):
            self.dic[ind+1] = image
        
    
    def create(self, tile_groups, enemy_groups):
            for i,row in enumerate(self.array):
                for j,tile in enumerate(row):
                    x = j * TILESIZE
                    y = i * TILESIZE
                    if tile == 'b':
                        Bat((x,y), enemy_groups)
                        continue
                    elif tile == 'p':
                        player = Player((x,y))
                        continue
                    elif tile > 0:
                        Tile((x,y), tile_groups, image = self.dic[tile])
            return player