# -*- coding: utf-8 -*-

import pygame
import sys
from settings import HEIGHT, WIDTH, FPS
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.image.load('src/Assets/Enviroments/Backgrounds/Al_bg.png')
        self.background = pygame.transform.scale(self.background,(WIDTH, HEIGHT))
        pygame.display.set_caption('BaldErDash')
        self.clock = pygame.time.Clock()
        self.iterator = 0
        self.level = Level(surface = self.screen, mapname = 'AW')

    def launch(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill('black')
            self.screen.blit(self.background, (self.iterator, 0))
            self.screen.blit(self.background,(WIDTH+self.iterator,0))
            if (self.iterator==-WIDTH):
                self.screen.blit(self.background,(WIDTH+self.iterator,0))
                self.iterator=0
            # завязать на движение
            self.iterator-=1
            self.level.launch()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.launch()