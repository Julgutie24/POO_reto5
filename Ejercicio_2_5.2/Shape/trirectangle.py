from .triangle import Triangle
from .point import Point

class TriRectangle(Triangle):
    def __init__(self, p1: Point, base: float, height: float):
        p2 = Point(p1.get_x() + base, p1.get_y())
        p3 = Point(p1.get_x(), p1.get_y() + height)
        super().__init__(p1, p2, p3)