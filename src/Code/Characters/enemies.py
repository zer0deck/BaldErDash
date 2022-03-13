import pygame
from Code.Characters.animation import Animation

class Bat(Animation):
    def __init__(self, pos, groups):
        animations = {'attack': [], 'fly': [], 'die': [], 'hang': []}
        self.status = 'fly'
        super().__init__(pos, groups, animations, ['Enemy', 'Bat'], self.status)
    
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
        super().__init__(pos, groups, animations, ['Enemy', 'Bee'], self.status)
    
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
        super().__init__(pos, groups, animations, ['Enemy', 'Big Boar'], self.status)
    
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
        super().__init__(pos, groups, animations, ['Enemy', 'Boar'], self.status)
    
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
        super().__init__(pos, groups, animations, ['Enemy', 'Goblin Axe'], self.status)
    
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
        super().__init__(pos, groups, animations, ['Enemy', 'Goblin Halberd'], self.status)

    
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
        super().__init__(pos, groups, animations, ['Enemy', 'Goblin Rider'], self.status)

    
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
        super().__init__(pos, groups, animations, ['Enemy', 'Goblin Spear'], self.status)
    
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
        super().__init__(pos, groups, animations, ['Enemy', 'Skeleton'], self.status)

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
        super().__init__(pos, groups, animations, ['Enemy', 'Skeleton Archer'], self.status)

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
        super().__init__(pos, groups, animations, ['Enemy', 'Skeleton Boss'], self.status)

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
        super().__init__(pos, groups, animations, ['Enemy', 'Skeleton Mage'], self.status)

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
        super().__init__(pos, groups, animations, ['Enemy', 'Skeleton Shield'], self.status)

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
        super().__init__(pos, groups, animations, ['Enemy', 'Skeleton Spear'], self.status)

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = 'attack'
        else:
            self.status = 'idle'
    
    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)