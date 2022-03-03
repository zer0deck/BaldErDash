import pygame
from settings import WIDTH, HEIGHT


class Background:
    def __init__(self, mapname, screen):
        self.background = pygame.image.load(f'src/Assets/Enviroments/Backgrounds/{mapname}_bg.png')
        self.background = pygame.transform.scale(self.background,(WIDTH, HEIGHT))
        self.screen = screen
        self.iterator = 0

    def update(self,shift):
        self.screen.fill('black')
        self.screen.blit(self.background, (self.iterator, 0))
        self.screen.blit(self.background,(WIDTH+self.iterator,0))
        self.screen.blit(self.background, (-WIDTH+self.iterator, 0))
        if (self.iterator==-WIDTH):
            self.screen.blit(self.background,(WIDTH+self.iterator,0))
            self.iterator=0
        elif (self.iterator==WIDTH):
            self.screen.blit(self.background,(-WIDTH-self.iterator,0))
            self.iterator=0            
        # завязать на движение
        self.iterator-=shift/4