# coding: utf-8


class Point(object):

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


__all__ = ["Point"]
