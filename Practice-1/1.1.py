def is_palindrome(n, temp=0):
    # Базовый случай для рекурсии
    if n == 0:
        return temp

    # Вычисление обратного числа
    temp = (temp * 10) + (n % 10)

    # Рекурсивный вызов функции с обновленными значениями
    return is_palindrome(n // 10, temp)

n = 12321
print(n == is_palindrome(n))  # Вывод: True

n = 12345
print(n == is_palindrome(n))  # Вывод: False
