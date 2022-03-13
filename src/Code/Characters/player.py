import pygame
from Code.settings import SPEED, TILESIZE, JUMPS, ATTACK_COOLDOWN, DASH_LENGTH, DASH_COOLDOWN
from Code.importer import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, type='Player Sword'):
        super().__init__()

        # set animation
        self.type = type
        self.assets()
        self.frame_index = 0
        # ! don't do animation speed aliquot to 1
        self.animation_speed = 0.3
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # player status
        self.facing = True
        self.space_pressed = False
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.can_jump = JUMPS

        # player actions status
        self.shift_pressed = False
        self.attacking = False
        self.attack_time = None
        self.dashing = False
        self.can_dash = True
        self.attack_type = 'attack_1'

        # cooldowns
        self.attack_cooldown = ATTACK_COOLDOWN
        self.dash_length = DASH_LENGTH
        self.dash_cooldown = DASH_COOLDOWN

        # movement params
        self.direction = pygame.math.Vector2(0,0)
        self.speed = SPEED
        self.gravity_v = SPEED/10
        self.jump_speed = -SPEED*2

    def assets(self):
        c_path = f'src/Assets/Sprites/Main_Character/{self.type}/'
        self.animations = {'climb': [], 'dash': [], 'die': [], 'fall': [], 'idle': [], 'jump': [], 'run': []}
        if self.type == 'Player Bow':
            self.animations['attack'] = []
        elif self.type == 'Player Spear' or 'Player Sword':
            self.animations['attack_1'] = []
            self.animations['attack_2'] = []
            self.animations['attack_3'] = []

        for animation in self.animations:
            path = c_path + animation
            self.animations[animation] = import_folder(path)

    def animate(self, status):
        animation = self.animations[status]
        self.frame_index += self.animation_speed

        if self.frame_index > len(animation)-1:
            if self.attacking == True:
                self.attacking = False
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
        if self.dashing:
            self.status = 'dash'
            self.animation_speed = 0.4
        elif self.attacking:
            self.animation_speed = 0.2
            self.status = self.attack_type
        else:
            self.animation_speed = 0.3
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

        # attack input
        if self.type != 'Player':
            if not self.attacking:
                if keys[pygame.K_e]:
                    self.attacking = True
                    self.attack_type = 'attack_1'
                    self.attack_time = pygame.time.get_ticks()
                    self.direction.x = 0
                    self.frame_index = 0

                elif keys[pygame.K_r]:
                    self.attacking = True
                    self.attack_type = 'attack_2'
                    self.attack_time = pygame.time.get_ticks()
                    self.frame_index = 0
                    self.direction.x = 0

                elif keys[pygame.K_t]:
                    self.attacking = True
                    self.attack_type = 'attack_3'
                    self.attack_time = pygame.time.get_ticks()
                    self.frame_index = 0
                    self.direction.x = 0


        # movement input
        if not self.dashing and not self.attacking:
            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.facing = True
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.facing = False
            else:
                self.direction.x = 0
            
            if self.can_dash:
                if keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT]:
                    self.dashing = True
                    self.facing = True
                    self.can_dash = False
                    self.dash_time = pygame.time.get_ticks()
                    self.direction.x = 2
                    self.frame_index = 0
                elif keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT]:
                    self.dashing = True
                    self.can_dash = False
                    self.facing = False
                    self.dash_time = pygame.time.get_ticks()
                    self.direction.x = -2
                    self.frame_index = 0

        # jump input

        if keys[pygame.K_SPACE]:
            if self.space_pressed == False:
                if self.can_jump > 0:
                    self.jump()
                self.space_pressed = True
        else:
            self.space_pressed = False


    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        # if self.attacking:
        #     if current_time - self.attack_time >= self.attack_cooldown:
        #         self.attacking = False

        if self.dashing:
            # self.direction.x = 2
            if current_time - self.dash_time >= self.dash_length:
                self.dashing = False
        if not self.can_dash:
            if current_time - self.dash_time >= self.dash_cooldown:
                self.can_dash = True

    def gravity(self):
        self.direction.y  += self.gravity_v
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        self.can_jump -= 1

    def update(self):
        self.input()
        self.cooldowns()
        self.rect.x += self.direction.x * self.speed
        # self.rect.x += self.momentum * self.speed
        self.get_status()
        self.animate(self.status)

