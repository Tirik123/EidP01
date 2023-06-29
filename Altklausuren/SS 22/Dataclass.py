from dataclasses import dataclass


@dataclass
class Shape:
    def bbox(self) -> 'Rectangle':
        raise Exception('bbox needs top be overriden by subclass of Shape')

# a)


@dataclass
class Point():
    x: int
    y: int

    def min(self, other):
        return Point(min(self.x, other.y), min(self.y, other.y))

    def max(self, other):
        return Point(max(self.x, other.y), max(self.y, other.y))

# b)


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
        min_Point = self.p_min.min(other.p_min)
        max_Point = self.p_max.max(other.p_max)
        return Rectangle(min_Point, max_Point)


@dataclass
class Triangle(Shape):
    left_corner: Point
    right_corner: Point
    upper_corner: Point

    def bbox(self, other) -> Rectangle:
        super().bbox()
        min_Point1 = (self.left_corner.min(other.left_corner), self.right_corner.min(other.right_corner))
        min_Point2 = (min_Point1, self.upper_corner.min(other.upper_corner))
        max_Point1 = (self.left_corner.max(other.left_corner), self.right_corner.max(other.right_corner))
        max_Point2 = (max_Point1, self.upper_corner.max(other.upper_corner))
        return Rectangle(min_Point2, max_Point2)
    

if __name__ == '__main__':
    p1 = Point(1, 100)
    p2 = Point(2, 20)
    print(p1.min(p2))
    print(p1.max(p2))

    r1 = Rectangle(Point(1, 1), Point(3, 3))
    r2 = Rectangle(Point(10, 10), Point(30, 30))
    print(r1.union(r2))

    t = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    #print(t.bbox())
