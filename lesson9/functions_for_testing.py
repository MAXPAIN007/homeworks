def sum_numbers_in_string(s):
    try:
        # Розділяємо рядок по комах і конвертуємо в числа
        numbers = [int(num) for num in s.split(",")]
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити!"

def calculate_average_of_int_list (int_list):
    if not int_list:
        return 0
    total_sum = sum(int_list)
    count = len(int_list)
    average = total_sum / count
    return average

def reverse_string(s: str) -> str:
    return s[::-1]

def longest_word(word_list):
    return max(word_list, key=len)

def sum_of_two_numbers (a: int, b: int) -> int:
    return a+b
