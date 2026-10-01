class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def __repr__(self):
        return f"{self.__class__.__name__}(width={self._width}, height={self._height})"

    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self._width == other._width and self._height == other._height

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() < other.get_area()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self.set_width(value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self.set_height(value)

    def set_width(self, width):
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Width must be a positive number.")
        self._width = width

    def set_height(self, height):
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be a positive number.")
        self._height = height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def get_diagonal(self):
        return (self._width**2 + self._height**2) ** 0.5

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        w = int(self._width)
        h = int(self._height)
        return ("*" * w + "\n") * h

    def get_amount_inside(self, shape):
        if not isinstance(shape, Rectangle):
            raise TypeError("Expected an instance of Rectangle or a subclass.")
        if shape.width <= 0 or shape.height <= 0:
            return 0
        return int(self._width // shape.width) * int(self._height // shape.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f"Square(side={self._width})"

    def __str__(self):
        return f"Square(side={self._width})"

    @property
    def side(self):
        return self._width

    @side.setter
    def side(self, value):
        self.set_side(value)

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

    def set_width(self, width):
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Side must be a positive number.")
        self._width = width
        self._height = width

    def set_height(self, height):
        self.set_width(height)