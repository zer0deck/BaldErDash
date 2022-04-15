import pygame

from ...Maps import dev
from ..Characters.enemies import Bat
from ..Characters.player import Player
from ..settings import TILESIZE
from .surface import Tile

__all__ = ["Map"]


class Map:
    def __init__(self, mapname):
        pygame.init()
        self.images = []
        self.array = []
        if mapname == "DevLevel":
            self.array, self.images = dev(TILESIZE)
        self.dic = {}
        for ind, image in enumerate(self.images):
            self.dic[ind + 1] = image

    def create(self, tile_groups, enemy_groups, player_attack):
        for i, row in enumerate(self.array):
            for j, tile in enumerate(row):
                x = j * TILESIZE
                y = i * TILESIZE
                if tile == "b":
                    Bat((x, y), enemy_groups)
                    continue
                elif tile == "p":
                    player = Player((x, y), player_attack)
                    continue
                elif tile > 0:
                    Tile((x, y), tile_groups, image=self.dic[tile])
        return player
