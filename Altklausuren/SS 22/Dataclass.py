from dataclasses import dataclass


@dataclass
class Shape:
    def bbox(self) -> 'Rectangle':
        raise Exception('bbox needs top be overriden by subclass of Shape')



#a)

@dataclass
class Point():
    x: int
    y: int



    def min(self, other):
        min_Point = min(self.x, other.x), min(self.y, other.y)
        return f'Point{min_Point}'
    
    def max(self, other):
        max_Point = max(self.x, other.x), max(self.y, other.y)
        return f'Point{max_Point}'
    
     

#b) 


@dataclass
class Rectangle(Shape):
    p_min: Point
    p_max: Point


    def __post_init__(self):
        assert self.p_min.x <= self.p_max.x and self.p_min.y <= self.p_max.y


    def bbox(self) -> 'Rectangle':
        super().bbox()
        return Rectangle(self.p_min, self.p_max)
    

    def union(self, other) -> 'Rectangle':
        return min(Rectangle(self.p_min.x, self.p_min.y), Rectangle(other.p_min.x, other.p_min.y))    






if __name__ == '__main__':
    p1 = Point(1, 100)
    p2 = Point(2, 20)
    print(p1.min(p2))
    print(p1.max(p2))

    r1 = Rectangle(Point(1, 1), Point(3, 3))
