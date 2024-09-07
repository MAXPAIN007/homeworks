from abc import ABC
from typing_extensions import override
from lesson16.part2.figure import Figure


class Square(Figure):

    __square_side:int

    def __init__(self, square_side:int):
        self.__square_side=square_side

    @override
    def area(self):
        return self.__square_side ** 2

    @override
    def perimeter(self):
        return 4 * self.__square_side
