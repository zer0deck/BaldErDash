# -*- coding: utf-8 -*-

import pygame
import sys
from settings import HEIGHT, WIDTH, FPS
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('BaldErDash')
        self.clock = pygame.time.Clock()
        self.level = Level(surface = self.screen, mapname = 'AW', screen = self.screen)

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