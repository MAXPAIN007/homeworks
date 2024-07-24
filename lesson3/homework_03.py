#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quote_count = alice_in_wonderland.count("'")
print("task 02 Кількість одинарних лапок у тексті:", single_quote_count)
single_quotes = [quote for quote in alice_in_wonderland if quote == "'"]
print("task 02 Символи одинарної лапки в тексті:", single_quotes)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print('task 03 \n', alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print('task 04\n' f'Чорне та Азовське моря разом займають {total_area} км².')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_items = 375291
stocks1and2 = 250449
stocks2and3 = 222950
stock1 = total_items - stocks2and3
stock3 = total_items - stocks1and2
stock2 = total_items - stock1 - stock3
print('task 05\n' f'Кількість товарів на першому складі {stock1} шт.\n'
      f'Кількість товарів на другому складі {stock2} шт.\n'
      f'Кількість товарів на третьому складі {stock3} шт.\n')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
period_in_months = 18
payment_in_month = 1179
total_price = period_in_months * payment_in_month
print('task 06\n' f'Вартість комп’ютера {total_price} грн.')

# task 07
"""
Знайди залишок від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
remainder_a = 8019 % 8
remainder_b = 9907 % 9
remainder_c = 2789 % 5
remainder_d = 7248 % 6
remainder_e = 7128 % 5
remainder_f = 19224 % 9
print('task 07\n' f'Залишок А = {remainder_a}\n'
      f'Залишок B = {remainder_b}\n'
      f'Залишок C = {remainder_c}\n'
      f'Залишок D = {remainder_d}\n'
      f'Залишок E = {remainder_e}\n'
      f'Залишок F = {remainder_f}\n')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_large_quantity = 4
pizza_large_price = 274
pizza_medium_quantity = 2
pizza_medium_price = 218
juice_quantity = 4
juice_price = 35
cake_quantity = 1
cake_price = 350
water_quantity = 3
water_price = 21
pizza_large_total = pizza_large_quantity * pizza_large_price
pizza_medium_total = pizza_medium_quantity * pizza_medium_price
juice_total = juice_quantity * juice_price
cake_total = cake_quantity * cake_price
water_total = water_quantity * water_price
total_amount = pizza_large_total + pizza_medium_total + juice_total + cake_total + water_total
print('task 08\n'f"Загальна сума замовлення: {total_amount} грн.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
import math
photos_quantity = 232
photos_per_page = 8
total_pages = math.ceil(photos_quantity / photos_per_page)
print('task 09\n'f"Ігорю знадобиться {total_pages} сторінок, щоб вклеїти всі фото.")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_km = 1600
fuel_in_tank_l = 48
consumption_per_100_km_l = 9
total_fuel_needed = int(distance_km * (consumption_per_100_km_l / 100))
refuelings_needed = math.ceil(total_fuel_needed / fuel_in_tank_l) - 1
print('task 09\n'f"Необхідна кількість бензину для подорожі: {total_fuel_needed} літрів\n"
      f"Необхідна кількість заправок: {refuelings_needed} ")
