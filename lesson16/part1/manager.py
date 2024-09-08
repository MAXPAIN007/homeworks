from lesson16.part1.employee import Employee


class Manager(Employee):

    _department:str

    def __init__(self, name:str, salary:int, department:str):
        super().__init__(name,salary)
        self._department=department
