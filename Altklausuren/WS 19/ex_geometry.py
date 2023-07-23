from dataclasses import dataclass

@dataclass
class Rect:
    x1: int
    y1: int
    x2: int
    y2: int


    def __eq__(self, other: 'Rect') -> bool:
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2
     



def merge(r1: Rect, r2: Rect):
    pass