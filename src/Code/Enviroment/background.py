import pygame

from ..settings import HEIGHT, WIDTH

__all__ = ["Background"]


class Background:
    def __init__(self, mapname, screen):
        mapname = "Forest"
        self.cloud = pygame.image.load(f"src/Assets/Backgrounds/{mapname}/bg_5.png")
        self.background = pygame.image.load(
            f"src/Assets/Backgrounds/{mapname}/bg_4.png"
        )
        self.middle = pygame.image.load(f"src/Assets/Backgrounds/{mapname}/bg_3.png")
        self.foreground = pygame.image.load(
            f"src/Assets/Backgrounds/{mapname}/bg_2.png"
        )
        self.cloud = pygame.transform.scale(self.cloud, (WIDTH, HEIGHT))
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.middle = pygame.transform.scale(self.middle, (WIDTH, HEIGHT))
        self.foreground = pygame.transform.scale(self.foreground, (WIDTH, HEIGHT))
        self.screen = screen
        self.screen.fill("black")
        self.iterC = 0
        self.iterB = 0
        self.iterM = 0
        self.iterF = 0

    def updateC(self, shift):
        self.screen.blit(self.cloud, (self.iterC, 0))
        self.screen.blit(self.cloud, (WIDTH + self.iterC, 0))
        self.screen.blit(self.cloud, (-WIDTH + self.iterC, 0))

        if self.iterC == -WIDTH:
            self.screen.blit(self.cloud, (WIDTH + self.iterC, 0))
            self.iterC = 0
        elif self.iterC == WIDTH:
            self.screen.blit(self.cloud, (-WIDTH - self.iterC, 0))
            self.iterC = 0

        self.iterC += shift / 10

    def updateB(self, shift):
        self.screen.blit(self.foreground, (self.iterB, 0))
        self.screen.blit(self.foreground, (WIDTH + self.iterB, 0))
        self.screen.blit(self.foreground, (-WIDTH + self.iterB, 0))

        if self.iterB == -WIDTH:
            self.screen.blit(self.background, (WIDTH + self.iterB, 0))
            self.iterB = 0
        elif self.iterB == WIDTH:
            self.screen.blit(self.background, (-WIDTH - self.iterB, 0))
            self.iterB = 0
        # завязать на движение
        self.iterB += shift / 8

    def updateM(self, shift):
        self.screen.blit(self.middle, (self.iterM, 0))
        self.screen.blit(self.middle, (WIDTH + self.iterM, 0))
        self.screen.blit(self.middle, (-WIDTH + self.iterM, 0))

        if self.iterM == -WIDTH:
            self.screen.blit(self.middle, (WIDTH + self.iterM, 0))
            self.iterM = 0
        elif self.iterM == WIDTH:
            self.screen.blit(self.middle, (-WIDTH - self.iterM, 0))
            self.iterM = 0
        # завязать на движение
        self.iterM += shift / 4

    def updateF(self, shift):
        self.screen.blit(self.foreground, (self.iterF, 0))
        self.screen.blit(self.foreground, (WIDTH + self.iterF, 0))
        self.screen.blit(self.foreground, (-WIDTH + self.iterF, 0))

        if self.iterF == -WIDTH:
            self.screen.blit(self.foreground, (WIDTH + self.iterF, 0))
            self.iterF = 0
        elif self.iterF == WIDTH:
            self.screen.blit(self.foreground, (-WIDTH - self.iterF, 0))
            self.iterF = 0
        # завязать на движение
        self.iterF += shift / 2

    def update(self, shift):
        self.updateC(shift)
        self.updateB(shift)
        self.updateM(shift)
        self.updateF(shift)
