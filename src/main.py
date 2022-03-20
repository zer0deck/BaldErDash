# -*- coding: utf-8 -*-

import pygame
import sys
from Code.settings import HEIGHT, WIDTH, FPS
from Code.Enviroment.level import Level

class Game:
    def __init__(self):
        pygame.init()
        flags = pygame.SCALED | pygame.RESIZABLE
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
        pygame.display.set_caption('BaldErDash')
        self.clock = pygame.time.Clock()
        self.level = Level(surface = self.screen, mapname = 'DevLevel')

    def launch(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.level.launch()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.launch()