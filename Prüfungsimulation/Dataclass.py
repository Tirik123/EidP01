from dataclasses import dataclass

@dataclass
class Name:
    surname: str
    prename: str

    def __lt__(self, other):
        if self.surname <= other.surname:
            return self.surname, self.prename
        elif self.surname == other.surname:
            if self.prename <= other.surname:
                return self.surname, self.prename
    
    

@dataclass
class MouseClick:
    x: int
    y: int


@dataclass
class KeyPress:
    key: str


Event = MouseClick | KeyPress


def log_event(event: Event):
    match event:
        case MouseClick(x, y):
            return f'Mouse clicked at ({x}, {y}).'
        case KeyPress(key):
            return f'Key' + '{key}' + 'pressed.'
        

@dataclass
class GameObjects:
    x: int
    y: int

    def move(self, dx: int, dy: int):
            self.x += dx
            self.y += dy
            return self.x, self.y
    
    def __post_init__(self):
        assert self.x > 0
        assert self.y > 0

@dataclass
class Player(GameObjects):
    health: int

    def __post_init__(self):
        assert self.health > 0
        return super().__post_init__()



# 10/20