'''Напишіть цикл, який буде вимагати від користувача ввести слово,
в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код.'''

is_correct_str: bool = False

while not is_correct_str:
    provide_word: str = input("Provide your word, please: ").lower()

    if provide_word.find("h") != -1:
        is_correct_str = True