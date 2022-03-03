

TILESIZE = 32
WIDTH = 1280
HEIGHT = 720
FPS = 60
SPEED = 5
GRAVITY = 2

def map(mapname):
    mapfile = open(f'src/Maps/{mapname}.txt', "r")
    MAP = mapfile.read().splitlines()
    for i, line in enumerate(MAP):
        MAP[i] = line.split('\t')
    mapfile.close()
    return MAP