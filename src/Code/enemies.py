import pygame
from importer import import_folder
from settings import SPEED

class Animation(pygame.sprite.Sprite):
    def __init__(self, pos, groups, animations, enemy, status, size = 1):
        super().__init__(groups)
        # animation 
        self.animations = animations
        self.enemy = enemy
        self.assets(size)
        self.frame_index = 0
        self.animation_speed = 0.3
        self.status = status
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # character status
        self.facing = True
        self.can_dash = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        # movement params
        self.direction = pygame.math.Vector2(0,0)
        self.speed = SPEED

    def assets(self, size):
        c_path = f'/Users/zer0deck/Documents/Документы/Git/BaldErDash/src/Assets/Sprites/Enemy/{self.enemy}/'

        for animation in self.animations:
            path = c_path + animation
            self.animations[animation] = import_folder(path, size)
    
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
    
    def shift(self, shift_speed):
        self.rect.x += shift_speed

class Bat(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'fly': [], 'die': [], 'hang': []}
        self.status = 'fly'
        super().__init__(pos, groups, animations, 'Bat', self.status)
    
    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'fly'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)

class Bee(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'idle': [], 'die': [], 'run': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Bee', self.status)
    
    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'dile'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)

class Big_Boar(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'idle': [], 'die': [], 'run': [], 'walk': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Big Boar', self.status)
    
    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)
    
class Boar(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'idle': [], 'die': [], 'run': [], 'walk': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Boar', self.status)
    
    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)

class Goblin_Axe(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'idle': [], 'die': [], 'run': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Goblin Axe', self.status)
    
    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)

class Goblin_Halberd(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'idle': [], 'die': [], 'run': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Goblin Halberd', self.status)

    
    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)
    
class Goblin_Rider(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'idle': [], 'die': [], 'run': [], 'walk': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Goblin Rider', self.status)

    
    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)

class Goblin_Spear(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'idle': [], 'die': [], 'run': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Goblin Spear', self.status)
    
    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)
    
class Skeleton(Animation):
    def __init__(self, pos, groups):
        animations = {'attack_1': [], 'attack_2': [], 'idle': [], 'die': [], 'run': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Skeleton', self.status)

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack_1'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)

class Skeleton_Archer(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'idle': [], 'die': [], 'run': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Skeleton Archer', self.status)

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)

class Skeleton_Boss(Animation):
    def __init__(self, pos, groups):
        animations = {'attack_1': [], 'attack_2': [], 'idle': [], 'die': [], 'run': [], 'stun': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Skeleton Boss', self.status)

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack_1'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)

class Skeleton_Mage(Animation):
    def __init__(self, pos, groups):
        animations = {'attack_1': [], 'attack_2': [], 'idle': [], 'die': [], 'run': [], 'teleport': [], 'teleport_reverse': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Skeleton Mage', self.status)

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack_1'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)

class Skeleton_Shield(Animation):
    def __init__(self, pos, groups):
        animations = {'attack_1': [], 'attack_2': [], 'attack_3': [], 'idle': [], 'die': [], 'run': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Skeleton Shield', self.status)

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack_1'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)

class Skeleton_Spear(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'idle': [], 'die': [], 'run': []}
        self.status = 'idle'
        super().__init__(pos, groups, animations, 'Skeleton Spear', self.status)

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)