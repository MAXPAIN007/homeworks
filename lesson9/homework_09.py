import unittest
from lesson9.functions_for_testing import sum_numbers_in_string
from lesson9.functions_for_testing import calculate_average_of_int_list
from lesson9.functions_for_testing import reverse_string
from lesson9.functions_for_testing import longest_word
from lesson9.functions_for_testing import sum_of_two_numbers

class MyTests(unittest.TestCase):

    def test_sum_numbers_in_string_positive(self):
        result = sum_numbers_in_string("10,20,30")
        assert result == 60, f"Expected 60, but got {result}"

    def test_sum_numbers_in_string_negative(self):
        result = sum_numbers_in_string("10,20,abd")
        assert result == "Не можу це зробити!", f"Expected 'Не можу це зробити!', but got {result}"

    def test_calculate_average_of_int_list_positive(self):
        result = calculate_average_of_int_list([10, 20, 30, 40, 50])
        assert result == 30.0, f"Expected 30.0, but got {result}"

    def test_calculate_average_of_int_list_negative(self):
        result = calculate_average_of_int_list([])
        assert result == 0, f"Expected 0, but got {result}"

    def test_reverse_string_positive(self):
        result = reverse_string("hello")
        assert result == "olleh", f"Expected 'olleh', but got {result}"

    def test_reverse_string_negative(self):
        result = reverse_string("")
        assert result == "", f"Expected an empty string, but got {result}"

    def test_longest_word_positive(self):
        result = longest_word(["apple", "banana", "cherry", "blueberry"])
        assert result == "blueberry", f"Expected 'blueberry', but got {result}"

    def test_longest_word_negative(self):
        try:
            result = longest_word([])
        except ValueError:
            result = "ValueError"
        assert result == "ValueError", f"Expected 'ValueError', but got {result}"

    def test_sum_of_two_numbers_positive(self):
        result = sum_of_two_numbers(5, 10)
        self.assertEqual(result,15), f"Expected 15, but got {result}"

    def test_sum_of_two_numbers_negative(self):
        result = sum_of_two_numbers(-3, 7)
        assert result == 4, f"Expected 4, but got {result}"


if __name__ == '__main__':
    unittest.main()
