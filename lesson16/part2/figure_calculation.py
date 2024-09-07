
from lesson16.part2.circle import Circle
from lesson16.part2.figure import Figure
from lesson16.part2.rectangle import Rectangle
from lesson16.part2.square import Square
from lesson16.part2.triangele import Triangle

square: Square=Square(10)

circle:Circle=Circle(5)

rectangle:Rectangle=Rectangle(5,6)

triangle:Triangle=Triangle(6,7,9)

figure_list:list[Figure]=[square,circle,rectangle,triangle]

list_tuple_perimeter_area:list[tuple[int,object]] = [(figure.area(),figure.perimeter()) for figure in figure_list]

for item in list_tuple_perimeter_area:
    print(item[0], item[1])