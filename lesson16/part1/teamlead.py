from lesson16.part1.developer import Developer
from lesson16.part1.manager import Manager


class TeamLead(Manager,Developer):

    team_size:int

    def __init__(self,name:str, salary:int, department:str, team_size:int):
        super().__init__(name,salary,department)
        self.team_size=team_size