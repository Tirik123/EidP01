from dataclasses import dataclass

# (a) #########################################################################

@dataclass(order=True)
class Name:
    surname: str
    prename: str


assert Name("A", "B") < Name("B", "A")
assert Name("A", "A") < Name("B", "B")
assert Name("A", "A") < Name("A", "B")
assert Name("B", "A") < Name("B", "B")


# Alternativ:

@dataclass
class NameAlt:
    surname: str
    prename: str

    def __lt__(self, other: 'NameAlt') -> bool:
        return (self.surname, self.prename) < (other.surname, other.prename)


assert NameAlt("A", "B") < NameAlt("B", "A")
assert NameAlt("A", "A") < NameAlt("B", "B")
assert NameAlt("A", "A") < NameAlt("A", "B")
assert NameAlt("B", "A") < NameAlt("B", "B")


# (b) #########################################################################

@dataclass
class MouseClick:
    x: int
    y: int


@dataclass
class KeyPress:
    key: str


Event = MouseClick | KeyPress


def log_event(e: Event):
    match e:
        case MouseClick(x, y):
            print(f"Mouse clicked at ({x}, {y}).")
        case KeyPress(key):
            print(f"Key '{key}' pressed.")


if __name__ == '__main__':
    for e in [MouseClick(23, 42), KeyPress('a')]:
        log_event(e)


# (c) #########################################################################

@dataclass
class GameObject:
    x: int
    y: int

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy
        assert self.x >= 0
        assert self.y >= 0

    def __post_init__(self):
        assert self.x >= 0
        assert self.y >= 0


@dataclass
class Player(GameObject):
    health: int

    def __post_init__(self):
        super().__post_init__()
        assert self.health >= 0


if __name__ == '__main__':
    Player(0, 0, 0)

    try:
        Player(-2, 3, 5)  # Code should already fail here with AssertionError.
        raise Exception
    except AssertionError as e:
        pass

    try:
        Player(2, -3, 5)
        raise Exception
    except AssertionError as e:
        pass

    try:
        Player(2, 3, -5)
        raise Exception
    except AssertionError as e:
        pass


# (b) #########################################################################


# (c) #########################################################################
