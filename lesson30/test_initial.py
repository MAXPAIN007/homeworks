import allure
import pytest

from lesson_18.test_log_decorator import logger


@allure.feature("This test class is for allure learning.")
class TestInitial:

    @allure.story("Test for sum function validation")
    @pytest.mark.parametrize("input_data, expected_output", [
        ([1, 2, 3], 6),
        ([-1, 0, 1], 0),
        ([10, 20, 30], 60)
    ])
    def test_sum(self, input_data, expected_output):
        logger.info("Starting of test case")
        assert sum(input_data) == expected_output

    @allure.story("Test for uppercase function validation")
    @pytest.mark.parametrize("input_string, expected_output", [
        ("hello", "HELLO"),
        ("world", "WORLD")
    ])
    def test_uppercase(self, input_string, expected_output):
        assert input_string.upper() == expected_output

    @allure.story("Test for issue vizualization")
    @allure.issue("https://jira/ticket/AQA-567", "Test was failed due to assertion")
    @pytest.mark.skip("Skip due to known issue")
    def test_issue(self):
        assert False