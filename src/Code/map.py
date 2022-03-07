import os, sys
import pygame
from surface import Tile
from player import Player
from settings import TILESIZE
from enemies import Bat

p = os.path.abspath('.')
sys.path.insert(1, p)
from src.Maps.Forest import forest

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
        
    
    def create(self, groups, enemies):
            for i,row in enumerate(self.array):
                for j,tile in enumerate(row):
                    x = j * TILESIZE
                    y = i * TILESIZE
                    if tile == 'b':
                        Bat((x,y), enemies)
                        continue
                    elif tile == 'p':
                        player = Player((x,y))
                        continue
                    elif tile > 0:
                        Tile((x,y), groups, image = self.dic[tile])
            return player