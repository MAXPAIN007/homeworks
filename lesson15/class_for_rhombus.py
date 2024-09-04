
class Rhombus:
    side_a=[]
    angle_a_between_sides_a_and_b=[]
    angle_b_adjacent_to_the_angle_a=[]


    def __init__(self, side_a: int, angle_a_between_sides_a_and_b: int, angle_b_adjacent_to_the_angle_a: int) -> None:
        self.side_a = side_a
        self.angle_a_between_sides_a_and_b = angle_a_between_sides_a_and_b
        self.angle_b_adjacent_to_the_angle_a = angle_b_adjacent_to_the_angle_a


    def __setattr__(self, key, value):
        if key == 'side_a':
            self.__set_side_a(value)
        elif key == 'angle_a_between_sides_a_and_b':
            self.__set_angle_a_between_sides_a_and_b(value)
        elif key == 'angle_b_adjacent_to_the_angle_a':
            self.__set_angle_b_adjacent_to_the_angle_a(value)
        else:
            super().__setattr__(key, value)


    def __set_side_a(self, value: int):
        if value > 0:
            super().__setattr__('side_a', value)
        else:
            raise ValueError("The side length must be greater than 0.")


    def __set_angle_a_between_sides_a_and_b(self, value: int):
        if 0 < value < 180:
            if hasattr(self, 'angle_b_adjacent_to_the_angle_a'):
                # Корректируем угол B, чтобы сумма была 180 градусов
                new_b = 180 - value
                if new_b + value != 180:
                    raise ValueError("The sum of the angles should be exactly 180 degrees.")
                super().__setattr__('angle_b_adjacent_to_the_angle_a', new_b)
            super().__setattr__('angle_a_between_sides_a_and_b', value)
        else:
            raise ValueError("The angle must be between 0 and 180 degrees.")


    def __set_angle_b_adjacent_to_the_angle_a(self, value: int):
        if 0 < value < 180:
            if hasattr(self, 'angle_a_between_sides_a_and_b'):
                # Корректируем угол A, чтобы сумма была 180 градусов
                new_a = 180 - value
                if new_a + value != 180:
                    raise ValueError("The sum of the angles should be exactly 180 degrees.")
                super().__setattr__('angle_a_between_sides_a_and_b', new_a)
            super().__setattr__('angle_b_adjacent_to_the_angle_a', value)
        else:
            raise ValueError("The angle must be between 0 and 180 degrees.")

    def get_info(self) -> str:
        return (f"Rhombus with side A {self.side_a} and angle A {self.angle_a_between_sides_a_and_b}° "
                    f"and angle B {self.angle_b_adjacent_to_the_angle_a}°.")



    # def __setattr__(self, key, value):
    #     if key == 'side_a':
    #         if value>0:
    #             super().__setattr__(key, value)
    #         else:
    #             raise ValueError("The side length must be greater than 0.")
    #
    #     elif key == 'angle_a_between_sides_a_and_b':
    #         if 0<value<180:
    #             if hasattr(self, 'angle_b_adjacent_to_the_angle_a'):
    #                 if value + self.angle_b_adjacent_to_the_angle_a > 180:
    #                     raise ValueError("The sum of the angles should not exceed 180 degrees.")
    #                 elif value + self.angle_b_adjacent_to_the_angle_a < 180:
    #                     raise ValueError("The sum of the angles should not be less than 180 degrees.")
    #                 elif value+ self.angle_b_adjacent_to_the_angle_a ==180:
    #                     super().__setattr__('angle_b_adjacent_to_the_angle_a', 180 - value)
    #             super().__setattr__(key, value)
    #         else:
    #             raise ValueError("The angle must be between 0 and 180 degrees.")
    #
    #     elif key == 'angle_b_adjacent_to_the_angle_a':
    #         if 0<value<180:
    #             if hasattr(self, 'angle_a_between_sides_a_and_b'):
    #                 if value + self.angle_a_between_sides_a_and_b > 180:
    #                     raise ValueError("The sum of the angles should not exceed 180 degrees.")
    #                 elif value + self.angle_a_between_sides_a_and_b < 180:
    #                     raise ValueError("The sum of the angles should not be less than 180 degrees.")
    #                 elif value+ self.angle_a_between_sides_a_and_b ==180:
    #                     super().__setattr__('angle_b_adjacent_to_the_angle_a', 180 - value)
    #             super().__setattr__(key, value)
    #         else:
    #             raise ValueError("The angle must be between 0 and 180 degrees.")
    #
    #     else:
    #         super().__setattr__(key, value)
    #
    # def get_info(self) -> str:
    #     return (f"Rhombus with side A {self.side_a} and angle A {self.angle_a_between_sides_a_and_b}° "
    #         f"and angle B {self.angle_b_adjacent_to_the_angle_a}°.")





    # def __set_angle_a_between_sides_a_and_b(self, value: int):
    #     if 0 < value < 180:
    #         if hasattr(self, 'angle_b_adjacent_to_the_angle_a'):
    #             total_angle = value + self.angle_b_adjacent_to_the_angle_a
    #             self.__validate_angles(total_angle)
    #         super().__setattr__('angle_a_between_sides_a_and_b', value)
    #
    #     else:
    #         raise ValueError("The angle must be between 0 and 180 degrees.")
    #
    # def __set_angle_b_adjacent_to_the_angle_a(self, value: int):
    #     if 0 < value < 180:
    #         if hasattr(self, 'angle_a_between_sides_a_and_b'):
    #             total_angle = value + self.angle_a_between_sides_a_and_b
    #             self.__validate_angles(total_angle)
    #         super().__setattr__('angle_b_adjacent_to_the_angle_a', value)
    #     else:
    #         raise ValueError("The angle must be between 0 and 180 degrees.")
    #
    # def __validate_angles(self, total_angle: int):
    #     if total_angle == 180:
    #         return
    #     elif total_angle > 180:
    #         raise ValueError("The sum of the angles should not exceed 180 degrees.")
    #     elif total_angle < 180:
    #         raise ValueError("The sum of the angles should not be less than 180 degrees.")


