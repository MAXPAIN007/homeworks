'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''

list_1: list [int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_result:int = sum([integer for integer in list_1 if integer % 2 == 0])
# sum_result: int = 0
# for integer in list_1:
#     if integer % 2 == 0:
#         sum_result += integer

print(sum_result)
