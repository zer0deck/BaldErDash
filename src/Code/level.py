import pygame
from settings import SPEED, WIDTH, HEIGHT
from background import Background
from map import Map
from debug import debug

class Level:
    def __init__(self, surface, mapname):
        
        # init screen
        self.display_surface = surface
        self.background = Background(mapname=mapname, screen=self.display_surface)

        self.world_shift = 0

        # init sprites groups
        self.player = pygame.sprite.GroupSingle()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # map creation
        self.create_level(mapname)

    def create_level(self, mapname):
        fmap = Map(mapname)
        player = fmap.create(groups=[self.visible_sprites, self.obstacle_sprites])
        self.player.add(player)

    def scroll(self):

        player = self.player.sprite
        x_pos = player.rect.centerx
        x_dir = player.direction.x
        

        if x_pos < WIDTH*0.4 and x_dir < 0:
            self.world_shift = SPEED
            player.speed = 0
            
        elif x_pos > WIDTH*0.6 and x_dir > 0:
            self.world_shift = -SPEED
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = SPEED

    def collision(self, direct):
        player = self.player.sprite

        if direct == 'h':
            player.rect.x += player.direction.x * player.speed

            # horizontal coll
            for sprite in self.obstacle_sprites.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left
        elif direct == 'v':
            player.gravity()

            # vertical coll
            for sprite in self.obstacle_sprites.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                    elif player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0    
        
        else: print('crash')

    def launch(self, debug_v = True):

        # background movement
        self.background.update(self.world_shift)

        # player movement
        self.player.draw(self.display_surface)
        self.player.update()
        self.collision('h')
        self.collision('v')

        # surface movement
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update(self.world_shift)

        self.scroll()

        #debug
        if debug_v == True:
            debug(self.player.sprite.direction)


