"""CQ08: Object Oriented Programming."""

from __future__ import annotations


class Point:
    """Creating Point class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Creating new Profile object."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutating to multiply - point."""
        self.x = self.x * factor
        self.y = self.y * factor 
    
    def scale(self, factor: int) -> Point:
        """Create a new point."""
        return Point(self.x * factor, self.y * factor)
        
# p1: Point = Point(2.0, 3.0)
# print(p1.x)
# print(p1.y)
# p1.scale_by(2)
# print("after scale_by: ")
# print(p1.x)
# print(p1.y)
# p2: Point = p1.scale(6)
# print("after scale:")
# print(p2.x)
# print(p2.y)