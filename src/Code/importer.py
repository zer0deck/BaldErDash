import pygame
from os import walk
from settings import TILESIZE

def import_folder(path):
    images = []
    for _,_,files in walk(path):
        for file in files:
            if file != '.DS_Store':
                f_path = f'{path}/{file}'
                print(f_path)
                image = pygame.transform.scale(pygame.image.load(f'{path}/{file}').convert_alpha(), (TILESIZE, TILESIZE))
                images.append(image)
    return images