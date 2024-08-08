# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # Exit the loop if the result is greater than 25
        if result > 25:
            break
        # Print the multiplication result in the correct format
        print(f"{number}x{multiplier}={result}")
        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_of_two_numbers (a: int, b: int) -> int:
    # sum=a+b
    # print(sum)
    return a+b
result: int = sum_of_two_numbers(5, 10)
print('task 02\n' f"{result}")



# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def calculate_average_of_int_list (int_list):
    if not int_list:
        return 0
    total_sum = sum(int_list)
    count = len(int_list)
    average = total_sum / count
    return average

int_list=[1,5,67,45,43,76875]
print('task 03\n' f"{calculate_average_of_int_list(int_list)}")



# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(s: str) -> str:
    return s[::-1]

input_string = "hello"
reversed_string = reverse_string(input_string)
print(f"Original string: {input_string}")
print(f"Reversed string: {reversed_string}))")



# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(word_list):
    return max(word_list, key=len)

words = ["apple", "bananaaa", "cherry", "date"]
longest = longest_word(words)
print(f"The longest word is: {longest}")



# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1



# task 7
'''Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
інакше - False. Строку отримати за допомогою функції input()
'''
def unique_counter(propose_string: str) -> bool:
    unique_count = len(set(propose_string))
    return unique_count > 10

propose_string: str = input("Provide your string here, please: ")
print(unique_counter(propose_string))



# task 8

# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

def input_year() -> int:
    while True:
        try:
            year = int(input("Enter the year (4 digits): "))
            if len(str(year)) != 4:
                raise ValueError("Year must be 4 digits.")
            return year
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def input_engine_capacity() -> float:
    while True:
        try:
            engine_capacity = float(input("Enter the engine capacity (e.g., 1.6): "))
            return engine_capacity
        except ValueError:
            print("Invalid input: Engine capacity must be a float (e.g., 1.6). Please try again.")


def input_mileage() -> int:
    while True:
        try:
            mileage = int(input("Enter the mileage (e.g., 36000): "))
            return mileage
        except ValueError:
            print("Invalid input: Mileage must be an integer. Please try again.")

def get_matching_cars(car_data, search_criteria):
    year_min, engine_volume_min, price_max = search_criteria
    matching_cars = [
        (key, value) for key, value in car_data.items()
        if value[1] >= year_min and value[2] >= engine_volume_min and value[4] <= price_max
    ]
    matching_cars_sorted = sorted(matching_cars, key=lambda x: x[1][4])
    return matching_cars_sorted[:5]

matching_cars = get_matching_cars(car_data, search_criteria)
for car in matching_cars:
    print(car)



# task 9
def check_sentences_starting_with_phrase(sentences: list[str], phrase: str = "By the time") -> bool:
    sentences_starting_with_phrase = [sentence.strip() for sentence in sentences if sentence.strip().startswith(phrase)]
    return bool(sentences_starting_with_phrase)

# Using this function:
adwentures_of_tom_sawer_sentences = [
    "By the time Tom reached the little isolated frame schoolhouse, he was out of the white alley.",
    "He seldom went to church.",
    "By the time he was finally noticed, he had been standing by the door for a while."
]
if check_sentences_starting_with_phrase(adwentures_of_tom_sawer_sentences):
    print("Речення починаються з 'By the time'.")
else:
    print("Жодне речення не починається з 'By the time'.")



# task 10
# Обчислює факторіал числа.

def factorial(number: int) -> int:
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""