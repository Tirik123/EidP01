from dataclasses import dataclass

@dataclass
class Shape:
    def bbox(self) -> 'Rectangle':
        raise Exception('bbox needs to be overriden by subclass of Shape!')
    

@dataclass
class Point:
    x: int
    y: int

    #a)

    def min(self, other: 'Point'):
        return Point(min(self.x, other.x), min(self.y, other.y))
    
    def max(self, other: 'Point'):
        return Point(max(self.x, other.x), max(self.y, other.y))
    
    '''def __le__(self, other: 'Point'):
        if min(self.x, other.x) <= min(self.y, other.y):
            return self.x <= other.y
    
    def __ge__(self, other: 'Point'):
        if max(self.x, other.x) >=  max(self.y, other.y):
            return self.x >= other.y'''
    


@dataclass
class Rectangle(Shape):
    p_min: Point
    p_max: Point


    def __post__init__(self):
        #assert self.p_min.min(self.p_max) <= self.p_min.max(self.p_max)
        assert self.p_min.x <= self.p_max.x and self.p_min.y <= self.p_max.y

    
    def bbox(self) -> 'Rectangle':
        return super().bbox()
    

    def union(self, other: 'Rectangle'):
        mini = self.p_min.min(other.p_min)
        maxi = self.p_max.max(other.p_max)
        return Rectangle(mini, maxi)
    


@dataclass
class Triangle(Shape):
    p1: Point
    p2: Point
    p3: Point

    def bbox(self) -> Rectangle:
        mini_1 = self.p1.min(self.p2)
        mini_2 = mini_1.min(self.p3)

        maxi_1 = self.p1.max(self.p2)
        maxi_2 = maxi_1.max(self.p3)
        return Rectangle(mini_2, maxi_2)




def bboxes(lst: list['Shape']) -> Rectangle:
    ...



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



#17/30
