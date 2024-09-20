

# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers(N):
    for i in range(0, N+1, 2):
        yield i

N = 10

for number in even_numbers(N):
    print(number)

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci_sequence(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

N = 74
print("Fibonacci sequence:")
for number in fibonacci_sequence(N):
    print(number)