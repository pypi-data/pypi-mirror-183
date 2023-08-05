# coding: utf-8

from typing import Union, Optional, NoReturn


class Point(object):

    def __init__(self, x: Optional[Union[float, int]] = None, y: Optional[Union[float, int]] = None):
        self.__x: float = 0
        self.__y: float = 0

        self.x = x
        self.y = y

    def get_x(self) -> Union[float, int]:
        return self.__x

    def set_x(self, value: Union[float, int]) -> NoReturn:
        if isinstance(value, (float, int)):
            self.__x = value

    x = property(get_x, set_x)

    def get_y(self) -> Union[float, int]:
        return self.__y

    def set_y(self, value: Union[float, int]) -> NoReturn:
        if isinstance(value, (float, int)):
            self.__y = value

    y = property(get_y, set_y)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


__all__ = ["Point"]


if __name__ == "__main__":
    pt = Point()
    assert str(pt) == "Point(0, 0)"
    pt.x = 3
    pt.y = None
    assert str(pt) == "Point(3, 0)"
    pt.y = 4
    assert str(pt) == "Point(3, 4)"
