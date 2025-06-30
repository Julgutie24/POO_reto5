from Shape.point import Point
from Shape.rectangle import Rectangle
from Shape.equilateral import Equilateral
from Shape.isosceles import Isosceles
from Shape.scalene import Scalene
from Shape.trirectangle import TriRectangle
from Shape.triangle import Triangle

# Crear puntos
p1 = Point(0, 0)
p2 = Point(3, 0)
p3 = Point(3, 4)
p4 = Point(0, 4)

# Rectangle
rect = Rectangle(p1, 3, 4)
print("Área del rectángulo:", rect.compute_area())
print("Perímetro del rectángulo:", rect.compute_perimeter())
print("Ángulos internos del rectángulo:", rect.compute_inner_angles())

# Triangle
tri = Triangle(p1, p2, p3)
print("Área del triángulo:", tri.compute_area())
print("Perímetro del triángulo:", tri.compute_perimeter())
print("Ángulos internos del triángulo:", tri.compute_inner_angles())

# Equilateral
eq = Equilateral(Point(0, 0), 5)
print("Área del triángulo equilátero:", eq.compute_area())
print("Perímetro del triángulo equilátero:", eq.compute_perimeter())
print("Ángulos internos del triángulo equilátero:", eq.compute_inner_angles())

# Isosceles
iso = Isosceles(Point(0, 0), 6, 4)
print("Área del triángulo isósceles:", iso.compute_area())
print("Perímetro del triángulo isósceles:", iso.compute_perimeter())
print("Ángulos internos del triángulo isósceles:", iso.compute_inner_angles())

# Scalene
sca = Scalene(p1, p2, p4)
print("Área del triángulo escaleno:", sca.compute_area())
print("Perímetro del triángulo escaleno:", sca.compute_perimeter())
print("Ángulos internos del triángulo escaleno:", sca.compute_inner_angles())

# TriRectangle
tri_rect = TriRectangle(Point(0, 0), 3, 4)
print("Área del triángulo rectángulo:", tri_rect.compute_area())
print("Perímetro del triángulo rectángulo:", tri_rect.compute_perimeter())
print("Ángulos internos del triángulo rectángulo:", tri_rect.compute_inner_angles())