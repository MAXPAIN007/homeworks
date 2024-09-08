from abc import ABC
from typing_extensions import override
from lesson16.part2.figure import Figure


class Rectangle(Figure):

    __width:int
    __height:int

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @override
    def area(self):
        return self.__width * self.__height

    @override
    def perimeter(self):
        return 2 * (self.__width + self.__height)