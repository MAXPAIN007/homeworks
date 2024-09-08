from abc import ABC
from typing_extensions import override
from lesson16.part2.figure import Figure
import math


class Circle(Figure):

    __radius:int

    def __init__(self, radius:int):
        self.__radius=radius

    @override
    def area(self):
        return math.pi * (self.__radius ** 2)

    @override
    def perimeter(self):
        return 2 * math.pi * self.__radius