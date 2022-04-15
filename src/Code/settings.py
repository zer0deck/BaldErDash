__all__ = [
    "TILESIZE",
    "WIDTH",
    "HEIGHT",
    "FPS",
    "SPEED",
    "JUMPS",
    "DASH_POWER",
    "DASH_COOLDOWN",
    "HEALTH",
    "ENERGY",
    "DAMAGE",
    "UI_FONT",
    "UI_FONT_SIZE",
    "WEAPON_DATA",
]


TILESIZE = 64
WIDTH = 1280
HEIGHT = 720
FPS = 60
SPEED = 4

JUMPS = 3
DASH_POWER = 1.5
DASH_COOLDOWN = 1200
HEALTH = 100
ENERGY = 60
DAMAGE = 10

# ui
ITEM_BOX_SIZE = 80
UI_FONT = "src/Assets/GUI/font.ttf"
UI_FONT_SIZE = 18
TEXT_COLOR = "#EEEEEE"

WEAPON_DATA = {
    "Player Bow": {
        "attack_1": {"cooldown": 1000, "damage": 15, "speed": 0.2},
        "attack_2": {"cooldown": 2000, "damage": 20, "speed": 0.2},
        "attack_3": {"cooldown": 3000, "damage": 30, "speed": 0.2},
    },
    "Player Sword": {
        "attack_1": {"cooldown": 1000, "damage": 15, "speed": 0.2},
        "attack_2": {"cooldown": 2000, "damage": 20, "speed": 0.2},
        "attack_3": {"cooldown": 3000, "damage": 30, "speed": 0.2},
    },
    "Player Spear": {
        "attack_1": {"cooldown": 100, "damage": 15, "speed": 0.2},
        "attack_2": {"cooldown": 200, "damage": 20, "speed": 0.2},
        "attack_3": {"cooldown": 300, "damage": 30, "speed": 0.2},
    },
}
