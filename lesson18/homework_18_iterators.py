# Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration ("Index out of iteration limits")
        value = self.lst[self.index]
        self.index -= 1
        return value

my_list = [10, 20, 30, 40, 50]
reverse_iter = ReverseIterator(my_list)

print("Reverse iterator")
for item in reverse_iter:
    print(item)


# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class EvenIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration ("Out of iteration limits")
        value = self.current
        self.current += 2
        return value

N = 10
even_iter = EvenIterator(N)
print("Paired number iterator")
for number in even_iter:
    print(number)