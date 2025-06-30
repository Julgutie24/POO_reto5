from .triangle import Triangle
from .point import Point
import math

class Equilateral(Triangle):
    def __init__(self, p1: Point, side_length: float):
        p2 = Point(p1.get_x() + side_length, p1.get_y())
        height = side_length * (math.sqrt(3) / 2)
        p3 = Point(p1.get_x() + side_length / 2, p1.get_y() + height)
        super().__init__(p1, p2, p3)
        self.set_is_regular(True)