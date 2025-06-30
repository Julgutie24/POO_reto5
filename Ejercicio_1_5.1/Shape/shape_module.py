import math

class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    #En esta funcion usamos math hypot que le hace un pitagoras para encontrar la distancia entre dos puntos
    # Podria ponerse tambien algo como sqrt(a**2 + b**2) pero no quise profe JHADSHJHJADHJDASHJ(lo quiero profe).
    def compute_distance(self, other):
        return math.hypot(self._x - other.get_x(), self._y - other.get_y())

class Line:
    def __init__(self, start_point: 'Point', end_point: 'Point'):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self.compute_length()

    def get_start_point(self):
        return self._start_point

    def set_start_point(self, value):
        self._start_point = value
        self._length = self.compute_length()

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, value):
        self._end_point = value
        self._length = self.compute_length()

    def get_length(self):
        return self._length

    def compute_length(self):
        return self._start_point.compute_distance(self._end_point)

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
            edge = Line(self._vertices[i], self._vertices[(i+1)%n]) #El %n sirve para cuando recorra el ultimo vertice, vuelva al primero y cierre la figurita.
            edges.append(edge)
        return edges

    def compute_area(self):
        raise NotImplementedError("Subclasses must implement compute_area()")

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self._edges)

    def compute_inner_angles(self):
        raise NotImplementedError("Subclasses must implement compute_inner_angles()")

class Rectangle(Shape):
    #Bottom_left es para definir un punto en la esquina inferior izquierda, desde ahi se traza el rectangulo.
    def __init__(self, bottom_left: Point, width: float, height: float):
        self._width = width
        self._height = height
        vertices = [
            bottom_left,
            Point(bottom_left.get_x() + width, bottom_left.get_y()),
            Point(bottom_left.get_x() + width, bottom_left.get_y() + height),
            Point(bottom_left.get_x(), bottom_left.get_y() + height)
        ]
    #Aqui usamos super para llamar a Shape y nos diga si es un cuadrado(alto = ancho)
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

class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__([p1, p2, p3])
#Aplicar la hermosa base*altura/2 tiene sus cosas...asi que hice una forma alternativa(herón)
#No es que sea muy dificil, pero es mas largo y no me gusta mucho(no queda lindo el codigito, de todas formas le dejo como seria).
    '''
si quisiera de forma base*altura/2:

def compute_area_base_height(self):
        # Tomamos el lado entre el primer y segundo vértice como base
        v = self.get_vertices()
        x1, y1 = v[0].get_x(), v[0].get_y()
        x2, y2 = v[1].get_x(), v[1].get_y()
        x3, y3 = v[2].get_x(), v[2].get_y()

        # Longitud de la base (A-B)
        base = math.hypot(x2 - x1, y2 - y1)

        # Altura desde C a la recta AB
        altura = abs((y2 - y1)*x3 - (x2 - x1)*y3 + x2*y1 - y2*x1) / math.hypot(y2 - y1, x2 - x1)

        return (base * altura) / 2
    '''
    def compute_area(self):
        a, b, c = [edge.get_length() for edge in self.get_edges()]
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

#Aqui realizamos ley de coseno de chill ([ \cos(A) = \frac{b^2 + c^2 - a^2}{2bc} ] )
    def compute_inner_angles(self):
        a, b, c = [edge.get_length() for edge in self.get_edges()]
        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_C = 180.0 - angle_A - angle_B
        self.set_inner_angles([angle_A, angle_B, angle_C])
        return self.get_inner_angles()

#Como es equilatero, pues le pedimos un primer punto y el tamaño de las caras, con eso armamos el dichoso.
class Equilateral(Triangle):
    def __init__(self, p1: Point, side_length: float):
        p2 = Point(p1.get_x() + side_length, p1.get_y())
        height = side_length * (math.sqrt(3) / 2)
        p3 = Point(p1.get_x() + side_length / 2, p1.get_y() + height)
        #Lo mandamos a Triangle para que haga su magia, y decimos que es regular porque claramente lo es.
        super().__init__(p1, p2, p3)
        self.set_is_regular(True)

class Isosceles(Triangle):
    def __init__(self, p1: Point, base: float, height: float):
        p2 = Point(p1.get_x() + base, p1.get_y())
        p3 = Point(p1.get_x() + base / 2, p1.get_y() + height)
        super().__init__(p1, p2, p3)
#Aqui practicamente es lo mismo que se hace en Triangle.
class Scalene(Triangle):
    pass

class TriRectangle(Triangle):
    def __init__(self, p1: Point, base: float, height: float):
        p2 = Point(p1.get_x() + base, p1.get_y())
        p3 = Point(p1.get_x(), p1.get_y() + height)
        super().__init__(p1, p2, p3)

# Ejemplo de uso de Point y Line
p1 = Point(0, 0)
p2 = Point(3, 0)
p3 = Point(3, 4)
p4 = Point(0, 4)

linea = Line(p1, p3)
print("Distancia entre p1 y p3:", p1.compute_distance(p3))
print("Longitud de la línea:", linea.get_length())

# Ejemplo de uso de Rectangle
rect = Rectangle(p1, 3, 4)
print("Área del rectángulo:", rect.compute_area())
print("Perímetro del rectángulo:", rect.compute_perimeter())
print("Ángulos internos del rectángulo:", rect.compute_inner_angles())

# Ejemplo de uso de Triangle
tri = Triangle(p1, p2, p3)
print("Área del triángulo:", tri.compute_area())
print("Perímetro del triángulo:", tri.compute_perimeter())
print("Ángulos internos del triángulo:", tri.compute_inner_angles())

# Ejemplo de uso de Equilateral
eq = Equilateral(Point(0, 0), 5)
print("Área del triángulo equilátero:", eq.compute_area())
print("Perímetro del triángulo equilátero:", eq.compute_perimeter())
print("Ángulos internos del triángulo equilátero:", eq.compute_inner_angles())

# Ejemplo de uso de Isosceles
iso = Isosceles(Point(0, 0), 6, 4)
print("Área del triángulo isósceles:", iso.compute_area())
print("Perímetro del triángulo isósceles:", iso.compute_perimeter())
print("Ángulos internos del triángulo isósceles:", iso.compute_inner_angles())

# Ejemplo de uso de Scalene
sca = Scalene(p1, p2, p4)
print("Área del triángulo escaleno:", sca.compute_area())
print("Perímetro del triángulo escaleno:", sca.compute_perimeter())
print("Ángulos internos del triángulo escaleno:", sca.compute_inner_angles())

# Ejemplo de uso de TriRectangle (triángulo rectángulo)
tri_rect = TriRectangle(Point(0, 0), 3, 4)
print("Área del triángulo rectángulo:", tri_rect.compute_area())
print("Perímetro del triángulo rectángulo:", tri_rect.compute_perimeter())
print("Ángulos internos del triángulo rectángulo:", tri_rect.compute_inner_angles())