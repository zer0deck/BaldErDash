import pygame
from surface import Object
from player import Player
from Maps.Forest import forest

class Map():
    def __init__(self, tilesize, mapname):
        pygame.init()
        self.tilesize = tilesize
        self.images = []
        self. array = []
        if mapname == 'Forest':
            self.array, self.images = forest(tilesize)
        self.dic = {}
        for ind, image in enumerate(self.images):
            self.dic[ind+1] = image
        
    
    def drawMap(self, groups, player):
            for i,row in enumerate(self.array):
                for j,tile in enumerate(row):
                    if tile == 'p':
                        psprite = Player((x,y), player[0], player[1], player[2], player[3])
                        continue
                    if tile > 0:
                        x = j * self.tilesize
                        y = i * self.tilesize
                        Object((x,y), groups, image = self.dic[tile])
                        # surface.blit(self.images[tile - 1], (location[0] + j * self.tilesize, location[1] + i * self.tilesize))
            return psprite