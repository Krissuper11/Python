"""Shapes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Constructor, sets the color."""
        self.color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        pass

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")
        return 0


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Constructor of the circle.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        self.radius = radius
        super().__init__(color)

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.radius}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return math.pi * self.radius * self.radius


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self.side = side
        super().__init__(color)

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.side}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.side * self.side


class Rectangle(Shape):
    """Rectangle is a subclass of Shape."""

    def __init__(self, color: str, side1: float, side2: float):
        """
        Constructor of the rectangle.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self.side1 = side1
        self.side2 = side2
        super().__init__(color)

    def __repr__(self) -> str:
        """
        Return representation of the rectangle.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.side1}, b: {self.side2}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Area of the square is side1 * side2.
        """
        return self.side1 * self.side2


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Constructor should create a list to store all the shapes."""
        self.shape_list = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.shape_list.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.shape_list

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total_area = 0
        for shape in self.shape_list:
            total_area += shape.get_area()
        return total_area

    def get_circles(self) -> list:
        """Return only circles."""
        return list(filter(lambda x: isinstance(x, Circle), self.shape_list))

    def get_squares(self) -> list:
        """Return only squares."""
        return list(filter(lambda x: isinstance(x, Square), self.shape_list))

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        pass


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(paint.get_circles())
