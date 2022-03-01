import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('src/Assets/Enviroments/Tilesets/AW/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.m = 1
        self.obstacle_sprites = obstacle_sprites

        self.isjump = False          

    def input(self):
        key = pygame.key.get_pressed()

        self.direction.y = 1
        if self.isjump == False:
            if key[pygame.K_SPACE]:
                self.isjump = True
        if self.isjump:
            F =(1 / 2)*self.m*(self.speed**2)
            self.direction.y -= F
            self.speed = self.speed-1
            if self.speed<0:
                self.m =-1
            if self.speed ==-6:
                self.isjump = False
                self.speed = 5
                self.m = 1        
        
        if key[pygame.K_RIGHT]:
            self.direction.x = 1
        elif key[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
              
    def move(self, speed):
        self.rect.x += self.direction.x * speed
        self.collision('h')
        self.rect.y += self.direction.y * speed
        self.collision('v')

    def collision(self, direction):
        if direction is 'h':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # left
                        self.rect.left = sprite.rect.right                  
        elif direction is 'v':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # up
                        self.rect.top = sprite.rect.bottom 

    def update(self):
        self.input()
        self.move(self.speed)