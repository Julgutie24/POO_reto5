import math
from .shape import Shape

class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        super().__init__([p1, p2, p3])

    def compute_area(self):
        a, b, c = [edge.get_length() for edge in self.get_edges()]
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def compute_inner_angles(self):
        a, b, c = [edge.get_length() for edge in self.get_edges()]
        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_C = 180.0 - angle_A - angle_B
        self.set_inner_angles([angle_A, angle_B, angle_C])
        return self.get_inner_angles()