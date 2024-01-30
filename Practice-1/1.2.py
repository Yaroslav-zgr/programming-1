def reverse_number(n):
    # Проверка, является ли число 8-битным целым числом со знаком
    if not -128 <= n <= 127:
        return "no solution"

    # Вычисление знака числа
    sign = -1 if n < 0 else 1
    n *= sign

    # Переворот числа
    reverse = int(str(n)[::-1])

    # Проверка, не выходит ли перевернутое число за пределы диапазона
    if not -128 <= reverse <= 127:
        return "no solution"

    # Возвращение перевернутого числа с учетом знака
    return reverse * sign

print(reverse_number(123))  # Вывод: "no solution"
print(reverse_number(-21))  # Вывод: -12
