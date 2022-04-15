import pygame

__all__ = ['dev']

def dev(tilesize):
    images = []
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Inside6.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Earthl2.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Earthr2.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerl5.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Floor7.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerl2.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerl8.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Flying4.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Earthr3.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Earthl3.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Earthr5.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Earthl5.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Ladder1.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Floor5.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Floor4.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerl1.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerl4.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerl3.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Floor9.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Flying5.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerr4.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Floor6.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerr5.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Earth5.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Earth4.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerl6.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Floor3.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Floor2.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerd1.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Ladder2.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerr11.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Insider1.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Inside1.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/insidel1.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Earthl1.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Earthr4.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Insider5.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Inside5.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Insidel5.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Trap1.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Cornerr9.png"), (tilesize, tilesize)).convert_alpha())
    images.append(pygame.transform.scale(pygame.image.load("src/Assets/Tilesets/.backForest/Floor1.png"), (tilesize, tilesize)).convert_alpha())

    array = [[0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [0,1,4,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [0,1,1,1,7,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [0,1,9,10,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [0,1,11,12,4,6,0,0,0,0,0,0,0,'b',0,0,0,0,0,0,0,0,13,14,15,16,0,0,0,0,3],
    [0,1,1,1,1,17,18,6,0,0,'p',0,19,0,0,0,0,20,0,0,0,13,21,17,21,4,22,22,22,22,23],
    [0,1,9,24,25,25,24,26,15,27,28,28,29,28,27,30,0,0,0,0,13,31,10,1,1,1,1,1,1,1,1],
    [0,1,2,32,33,33,33,34,3,1,1,1,1,1,1,2,0,0,0,13,31,35,36,10,1,1,1,1,1,1,1],
    [1,1,2,37,38,38,38,39,3,1,1,1,1,1,1,11,40,40,40,12,17,41,0,3,1,1,1,1,1,1,1],
    [0,1,17,42,27,28,42,27,21,1,1,1,1,1,1,1,1,1,1,1,1,17,27,21,1,1,1,1,1,1,1]]

    return array, images
