from .shape import Shape
from .point import Point

class Rectangle(Shape):
    def __init__(self, bottom_left: Point, width: float, height: float):
        self._width = width
        self._height = height
        vertices = [
            bottom_left,
            Point(bottom_left.get_x() + width, bottom_left.get_y()),
            Point(bottom_left.get_x() + width, bottom_left.get_y() + height),
            Point(bottom_left.get_x(), bottom_left.get_y() + height)
        ]
        super().__init__(vertices, is_regular=(width == height))

    def get_width(self):
        return self._width

    def set_width(self, value):
        self._width = value

    def get_height(self):
        return self._height

    def set_height(self, value):
        self._height = value

    def compute_area(self):
        return self._width * self._height

    def compute_inner_angles(self):
        self.set_inner_angles([90.0, 90.0, 90.0, 90.0])
        return self.get_inner_angles()