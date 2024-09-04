
class Students:
    def __init__(self, first_name:str, last_name:str, age:int, grade_point_average:float):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade_point_average = grade_point_average

    def update_average_grade(self, new_grade: float):
        self.grade_point_average = new_grade

    def display_info(self):
        print(f"Ім'я: {self.first_name}")
        print(f"Прізвище: {self.last_name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.grade_point_average}")