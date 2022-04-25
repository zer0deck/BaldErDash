from os import walk

import pygame

from .settings import TILESIZE

__all__ = ["import_folder"]


def import_folder(path, size_coef=0.4):
    images = []
    for _, _, files in walk(path):
        for file in files:
            if file != ".DS_Store":
                im = pygame.image.load(f"{path}/{file}")
                image = pygame.transform.smoothscale(
                    im,
                    (im.get_width() * size_coef, im.get_height() * size_coef),
                )
                # image = pygame.image.load(f'{path}/{file}').convert_alpha()
                images.append(image)
    return images
