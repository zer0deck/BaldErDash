import pygame
from Code.settings import SPEED, TILESIZE
from Code.importer import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # set animation
        self.assets()
        self.frame_index = 0
        # ! don't do animation speed aliquot to 1
        self.animation_speed = 0.3
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # player status
        self.facing = True
        self.can_dash = True
        self.space_pressed = False
        self.shift_pressed = False
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.can_jump = 2

        # movement params
        self.direction = pygame.math.Vector2(0,0)
        self.speed = SPEED
        self.gravity_v = SPEED/10
        self.jump_speed = -SPEED*2
        self.momentum = 0
        self.mom_tick = 0
        self.route = 0

    def assets(self):
        c_path = 'src/Assets/Sprites/Main_Character/Player/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'dash': [], 'climb': [], 'die':[], 'fall': []}

        for animation in self.animations:
            path = c_path + animation
            self.animations[animation] = import_folder(path)

    def animate(self, status):
        animation = self.animations[status]
        self.frame_index += self.animation_speed

        if self.frame_index > len(animation):
            self.frame_index = 0
        
        if self.facing:
            self.image = animation[int(self.frame_index)]
        else:
            self.image = pygame.transform.flip(animation[int(self.frame_index)], True, False)
        
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def get_status(self):
        if self.route != 0 and self.can_dash == False:
            self.status = 'dash'
        else:
            if self.direction.y < 0:
                self.status = 'jump'
            elif self.direction.y > 1:
                self.status = 'fall'
            else: 
                if self.direction.x != 0:
                    self.status = 'run'
                else:
                    self.status = 'idle'

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys [pygame.K_d]:
            self.direction.x = 1
            self.facing = True
        elif keys[pygame.K_LEFT] or keys [pygame.K_a]:
            self.direction.x = -1
            self.facing = False
        else:
            self.direction.x = 0
        

        if keys[pygame.K_LSHIFT] and (keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_d]):
            if self.shift_pressed == False:
                if self.can_dash:
                    if self.facing:
                        self.route = 1
                        
                    else:
                        self.route = -1
                    self.can_dash = False
                self.shift_pressed = True
        else:
            self.shift_pressed = False
            self.route = 0
            # self.can_dash = True


        if keys[pygame.K_SPACE]:
            if self.space_pressed == False:
                if self.can_jump > 0:
                    self.jump()
                self.space_pressed = True
        else:
            self.space_pressed = False
    
    def gravity(self):
        self.direction.y  += self.gravity_v
        self.rect.y += self.direction.y

        # dash
        if not self.can_dash:
            self.mom_tick += 1
            self.momentum = self.route * 2
        if self.mom_tick >= 15:
            self.momentum = 0 
            self.mom_tick = 0
            self.can_dash = True

    def jump(self):
        self.direction.y = self.jump_speed
        self.can_jump -= 1

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.rect.x += self.momentum * self.speed
        self.get_status()
        self.animate(self.status)

