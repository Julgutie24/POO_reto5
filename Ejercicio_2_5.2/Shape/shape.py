from .line import Line

class Shape:
    def __init__(self, vertices: list, is_regular: bool = False):
        self._is_regular = is_regular
        self._vertices = vertices
        self._edges = self._compute_edges()
        self._inner_angles = []

    def get_is_regular(self):
        return self._is_regular

    def set_is_regular(self, value):
        self._is_regular = value

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, value):
        self._vertices = value
        self._edges = self._compute_edges()

    def get_edges(self):
        return self._edges

    def get_inner_angles(self):
        return self._inner_angles

    def set_inner_angles(self, value):
        self._inner_angles = value

    def _compute_edges(self):
        edges = []
        n = len(self._vertices)
        for i in range(n):
            edge = Line(self._vertices[i], self._vertices[(i+1)%n])
            edges.append(edge)
        return edges

    def compute_area(self):
        raise NotImplementedError

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self._edges)

    def compute_inner_angles(self):
        raise NotImplementedError