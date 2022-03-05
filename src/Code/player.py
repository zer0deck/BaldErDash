import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, obstacle_sprites, speed, gravity):
        super().__init__(group)
        self.image = pygame.image.load('src/Assets/Sprites/Main_Character/Player/run/player_run_00.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.canjump = True
        self.direction = pygame.math.Vector2()
        self.speed = speed
        self.gravity = self.speed
        self.temp_height = None
        self.obstacle_sprites = obstacle_sprites

        self.isjump = False       

    def input(self):
        key = pygame.key.get_pressed()

        if self.canjump == True:
            self.direction.y = self.speed
            if key[pygame.K_SPACE] or key[pygame.K_UP]:
                self.temp_height = self.rect.y
                self.direction.y = -self.gravity
                self.canjump = False
        if self.temp_height != None:
            if self.temp_height - self.rect.y < 100:
                self.direction.y = -self.gravity
            else:
                self.temp_height = None
                self.direction.y = self.gravity 

        
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.direction.x = self.speed
        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.direction.x = -self.speed
        else:
            self.direction.x = 0
              
    def move(self, speed, gravity):
        # if self.direction.y < 0:
        #     if self.direction.magnitude() != 0:
        #         self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        self.collision('h')

        self.rect.y += self.direction.y * gravity
        self.collision('v')

    def collision(self, direction):
        if direction == 'h':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # right
                        self.rect.right = sprite.rect.left
                    elif self.direction.x < 0: # left
                        self.rect.left = sprite.rect.right                  
        elif direction == 'v':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # down
                        self.rect.bottom = sprite.rect.top
                        self.canjump = True
                    if self.direction.y < 0: # up
                        self.rect.top = sprite.rect.bottom 

    def update(self):
        self.input()
        self.move(self.speed, self.gravity)