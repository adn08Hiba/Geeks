import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Must provide radius or diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f})"

    def __add__(self, other):
        if isinstance(other, Circle):
            # Add the radii to get a new circle radius
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return math.isclose(self.radius, other.radius)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

# Example usage:

c1 = Circle(radius=3)
c2 = Circle(diameter=10)

print(c1)                      # Circle(radius=3.00, diameter=6.00)
print(c2)                      # Circle(radius=5.00, diameter=10.00)
print(f"Area of c1: {c1.area():.2f}")
print(f"Area of c2: {c2.area():.2f}")

c3 = c1 + c2
print(f"Added circle: {c3}")    # Circle(radius=8.00, diameter=16.00)

print(c1 > c2)                 # False
print(c1 == c2)                # False
print(c1 < c2)                 # True

circles = [c2, c1, c3]
circles.sort()                 # sorts by radius due to __lt__

print("Sorted circles:")
for c in circles:
    print(c)
