# Aufgabe 4 (Dataclasses) #####################################################

from dataclasses import dataclass


# (a) #########################################################################
dataclass
class Name():
    surname: str
    prename: str

    def __lt__(self, other):
        if self.surname == other:
            return self.prename < other
        return self.surname < other



# (b) #########################################################################
dataclass
class MouseClick():
    x: int
    y: int


class KeyPress():
    key: str


Event = MouseClick | KeyPress


def log_event(event: Event):
    match event:
        case MouseClick(x, y):
            print(f" Mouse clicked at ({x}, {y}).")
        case KeyPress(k):
            print(f"Key '{k}' pressed.")


# (c) #########################################################################
dataclass
class GameObjects():
    x: int
    y: int

    def __post_init__(self):
        assert self.x >= 0
        assert self.y >= 0

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy


dataclass
class Player(GameObjects):
    health: int

    def __post_init__(self):
        assert self.health > 0
        super().__post_init__()
    
    def move(self, dx: int, dy: int):
        return super().move(dx, dy)




