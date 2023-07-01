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
        return Point(min(self.x, other.x), min(self.y, other.y))

    def max(self, other):
        return Point(max(self.x, other.x), max(self.y, other.y))

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

    def bbox(self) -> Rectangle:
        #super().bbox()
        min_Point_left_right = (self.left_corner.min(self.right_corner))
        min_Point_upper_left_right = (self.upper_corner.min(min_Point_left_right))
        max_Point_left_right = (self.left_corner.max(self.right_corner))
        max_Point_upper_left_right = (self.upper_corner.max(max_Point_left_right))
        return Rectangle(min_Point_upper_left_right, max_Point_upper_left_right)
    


'''def bboxes(geo_list: list['Shape']) -> 'Rectangle':
    rectangle = Rectangle
    triangle = Triangle
    for geo in geo_list:
        if geo == Triangle:
            triangle_bbox = geo.bbox()
        elif geo == Rectangle:
            rectangle_bbox = geo.union()
    return Rectangle(geo.min(geo), geo.max(geo))'''

    

if __name__ == '__main__':
    p1 = Point(1, 100)
    p2 = Point(2, 20)
    print(p1.min(p2))
    print(p1.max(p2))

    r1 = Rectangle(Point(1, 1), Point(3, 3))
    r2 = Rectangle(Point(10, 10), Point(30, 30))
    print(r1.union(r2))

    t = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(t.bbox())
