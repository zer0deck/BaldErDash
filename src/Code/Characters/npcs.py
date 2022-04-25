from .animation import Animation

__all__ = ["NPC_1", "NPC_2", "NPC_3", "NPC_Blacksmith", "NPC_Merchant"]


class NPC_1(Animation):
    def __init__(self, pos, groups):
        animations = {"idle": [], "jump": [], "run": []}
        self.status = "idle"
        super().__init__(
            pos, groups, animations, ["NPC", "NPC_1"], self.status, size=0.4
        )
        self.text = "Hi"

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = "run"
        else:
            self.status = "idle"

    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)


class NPC_2(Animation):
    def __init__(self, pos, groups):
        animations = {"idle": [], "jump": [], "run": []}
        self.status = "idle"
        super().__init__(
            pos, groups, animations, ["NPC", "NPC_2"], self.status, size=0.4
        )
        self.text = "Hi"

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = "run"
        else:
            self.status = "idle"

    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)


class NPC_3(Animation):
    def __init__(self, pos, groups):
        animations = {"idle": [], "jump": [], "run": []}
        self.status = "idle"
        super().__init__(
            pos, groups, animations, ["NPC", "NPC_3"], self.status, size=0.4
        )
        self.text = "Hi"

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = "run"
        else:
            self.status = "idle"

    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)


class NPC_Blacksmith(Animation):
    def __init__(self, pos, groups):
        animations = {"Action_1": [], "Action_2": []}
        self.status = "Action_1"
        super().__init__(
            pos, groups, animations, ["NPC", "NPC_Blacksmith"], self.status, size=0.4
        )
        self.text = "Hi"

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = "Action_2"
        else:
            self.status = "Action_1"

    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)


class NPC_Merchant(Animation):
    def __init__(self, pos, groups):
        animations = {"idle": [], "run": []}
        self.status = "idle"
        super().__init__(
            pos, groups, animations, ["NPC", "NPC_Merchant"], self.status, size=0.4
        )
        self.text = "Hi"

    def get_status(self):
        if self.direction.x != 0 or self.direction.y != 0:
            self.status = "run"
        else:
            self.status = "idle"

    def update(self, speed):
        self.shift(speed)
        self.get_status()
        self.animate(self.status)
