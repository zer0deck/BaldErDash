import pygame
from os import walk
from Code.settings import TILESIZE

def import_folder(path, size_coef=1):
    images = []
    for _,_,files in walk(path):
        for file in files:
            if file != '.DS_Store':
                image = pygame.transform.scale(pygame.image.load(f'{path}/{file}').convert_alpha(), (TILESIZE*size_coef, TILESIZE*size_coef))
                # image = pygame.image.load(f'{path}/{file}').convert_alpha()
                images.append(image)
    return images