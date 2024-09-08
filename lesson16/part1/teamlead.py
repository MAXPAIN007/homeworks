from lesson16.part1.manager import Manager
from lesson16.part1.developer import Developer



class TeamLead(Manager,Developer):

    _team_size:int

    def __init__(self,name:str, salary:int, department:str, team_size:int):
        super().__init__(name,salary,department)
        self._team_size=team_size

