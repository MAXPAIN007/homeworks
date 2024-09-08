

class Employee:

    _name:str
    _salary:int

    def __init__(self, name:str, salary:int):
        self._name=name
        self._salary=salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_name(self, name: str):
        self._name = name

    def set_salary(self, salary: int):
        self._salary = salary
