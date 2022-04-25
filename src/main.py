# -*- coding: utf-8 -*-

# TODO LIST:
# 1. Add NPC interactions
# 2. Add enemies AI
# 3. Add levels
# 4. Fix assets
# 5. Add more UI
# 6. Add story
# 7. Add player progress ability

import os
import shutil
import sys

import pygame

from .Code.Enviroment.level import Level
from .Code.settings import FPS, HEIGHT, WIDTH


class Game:
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        if "Assets" not in os.listdir(self.path):
            print(
                "\nDo you want to load the assets pack?\nThis may require internet connection.\n\n"
            )
            answer = input("[y/n]")
            if answer == "y":
                import zipfile

                import wget

                print("Beginning file download with wget module")
                wget.download(
                    "zer0deck.ru/balderdash/assetspack.zip",
                    f"{self.path}/assetspack.zip",
                )
                z_f = zipfile.ZipFile(f"{self.path}/assetspack.zip")
                z_f.extractall(f"{self.path}/Assets")
                z_f.close()
                os.remove(f"{self.path}/assetspack.zip")
        pygame.init()
        flags = pygame.SCALED | pygame.RESIZABLE
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
        pygame.display.set_caption("BaldErDash")
        self.clock = pygame.time.Clock()
        self.level = Level(surface=self.screen, mapname="DevLevel")

    def launch(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pathes = [
                        f"{self.path}/Maps/__pycache__",
                        f"{self.path}/Code/Characters/__pycache__",
                        f"{self.path}/Code/__pycache__",
                        f"{self.path}/Code/Enviroment/__pycache__",
                        f"{self.path}/__pycache__",
                    ]
                    for path in pathes:
                        try:
                            shutil.rmtree(path)
                        except:  # OSError as e:
                            # print("Error: %s : %s" % (path, e.strerror))
                            continue

                    sys.exit()

            self.level.launch()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.launch()
