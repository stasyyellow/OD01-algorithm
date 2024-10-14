def is_palindrome(s):
    # Шаг 1: Приводим строку к нижнему регистру
    s = s.lower()

    # Шаг 2: Удаляем все пробелы из строки
    s = s.replace(" ", "")

    # Шаг 3: Сравниваем строку с её обратной версией
    return s == s[::-1]

# список строк для тестирования
test_strings = [
    "финик",
    "Заказ",
    "ТопоТ",
    "доХод",
    "madam",
    "мимика"
]

# тестируем функцию
for test_str in test_strings:
    if is_palindrome(test_str):
        print(f'"{test_str}" — это палиндром.')
    else:
        print(f'"{test_str}" — это не палиндром.')

