'''Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
інакше - False. Строку отримати за допомогою функції input()
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код.'''

propose_string: str = input("Provide your string here, please: ")
unique_counter: int = sum([1 for char in propose_string if propose_string.count(char) == 1])

# unique_counter: int = 0
# for char in propose_string:
#     if propose_string.count(char) == 1:
#         unique_counter += 1

if unique_counter > 10:
    print(True)
else:
    print(False)