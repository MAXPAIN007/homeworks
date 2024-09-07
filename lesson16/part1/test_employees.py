from assertpy import assert_that

from lesson16.part1.teamlead import TeamLead


class TestEmployees:

    qa_automation_team_lead:TeamLead=TeamLead("Ben", 1500, "BestTest Department", 15)

    expected_result:dict[str,object]={
        "name":"Ben",
        "salary":1500,
        "department":"BestTest Department",
        "team_size":15
    }

    def test_employee_attrs(self):

        (assert_that(self.qa_automation_team_lead.__dict__,"Desired user's attributes are not equal to desired dict to attributes").is_equal_to(self.expected_result))


    # MY VERSION
    # def test_team_lead_attributes(self):
    #     # Створення об'єкта TeamLead
    #     team_lead:TeamLead = TeamLead("Alice", 100000, "IT",  5)
    #
    #     # Перевірка наявності атрибутів
    #     assert hasattr(team_lead, 'name'), "Атрибут 'name' відсутній у класі TeamLead"
    #     assert hasattr(team_lead, 'salary'), "Атрибут 'salary' відсутній у класі TeamLead"
    #     assert hasattr(team_lead, 'department'), "Атрибут 'department' відсутній у класі TeamLead"
    #     assert hasattr(team_lead, 'team_size'), "Атрибут 'team_size' відсутній у класі TeamLead"
    #
    #     print("Усі атрибути присутні у класі TeamLead.")




