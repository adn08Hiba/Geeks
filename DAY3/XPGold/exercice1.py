import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def get_perimeter(self):
        """Calcule le périmètre du cercle (2πr)."""
        return 2 * math.pi * self.radius

    def get_area(self):
        """Calcule l'aire du cercle (πr²)."""
        return math.pi * (self.radius ** 2)

    def definition(self):
        print("A circle is a shape with all points the same distance from its center.")
# Créer un cercle avec rayon 3
c = Circle(3)

print(f"Radius: {c.radius}")
print(f"Perimeter: {c.get_perimeter():.2f}")
print(f"Area: {c.get_area():.2f}")
c.definition()
