import functools
import time


# Напишіть декоратор, який логує аргументи та результати викликаної функції.
def log_arguments_and_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Викликається функція: {func.__name__}")
        print(f"Аргументи: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper


@log_arguments_and_result
def add(a, b):
    return a + b

result = add(5, 3)


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def retry_on_exception(retries=3, delay=1, exceptions=(Exception,), default=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    print(f"Виняток у функції {func.__name__}: {e}. Спроба {attempts} з {retries}.")
                    if attempts < retries:
                        time.sleep(delay)  # Затримка перед повторною спробою
            # Якщо всі спроби провалилися, повертаємо значення за замовчуванням
            return default
        return wrapper
    return decorator

@retry_on_exception(retries=3, delay=2, exceptions=(ZeroDivisionError,), default="Невдача")
def divide(a, b):
    return a / b

result_2 = divide(10, 0)
print(result_2)
