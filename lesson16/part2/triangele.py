from abc import ABC
from typing_extensions import override
from lesson16.part2.figure import Figure
import math


class Triangle(Figure):

    __side_a:int
    __side_b:int
    __side_c:int

    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    @override
    def area(self):
        s = (self.__side_a + self.__side_b + self.__side_c) / 2
        return math.sqrt(s * (s - self.__side_a) * (s - self.__side_b) * (s - self.__side_c))

    @override
    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c