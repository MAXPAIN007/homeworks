# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

def sum_numbers_in_string(s):
    try:
        # Розділяємо рядок по комах і конвертуємо в числа
        numbers = [int(num) for num in s.split(",")]
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити!"

strings_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in strings_list:
    result = sum_numbers_in_string(item)
    print(f"Variant 1 {result}")



strings_list1 = ["1,2,3,4", "1,2,3,4,50", "1,2,3"]
def sum_all_chars_in_string_if_int (test_list: list) -> None:
    result: list[int] = list()
    try:
        for item in test_list:
            chars_list: list = item.split(",")
            result.append(sum(int(integer) for integer in chars_list))
    except ValueError as exception:
        print(f"I can not sum your items list due to: {exception}")
    else:
        print(f"Variant 2 {result}")

sum_all_chars_in_string_if_int(strings_list1)



# def sum_all_chars_in_string_if_int(test_list: list) -> None:
#     try:
#         result = [sum(int(integer) for integer in item.split(",")) for item in test_list]
#     except ValueError as exception:
#         print(f"I can not sum your items from list due to: {exception}")
#     else:
#         print(result)