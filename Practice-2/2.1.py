
def longest_substring(s):
    # Инициализация словаря для хранения последнего индекса каждого символа
    last_seen = {}
    # Инициализация начальной точки подстроки
    start = 0
    # Инициализация максимальной длины
    max_length = 0
    # Инициализация подстроки с максимальной длиной
    max_substring = ""

    # Проходим по всем символам в строке
    for i, char in enumerate(s):
        # Если символ уже встречался и его индекс больше или равен начальной точке подстроки
        if char in last_seen and last_seen[char] >= start:
            # Обновляем начальную точку подстроки
            start = last_seen[char] + 1
        else:
            # Если текущая длина подстроки больше максимальной
            if i - start + 1 > max_length:
                # Обновляем максимальную длину
                max_length = i - start + 1
                # Обновляем подстроку с максимальной длиной
                max_substring = s[start:i+1]

        # Обновляем последний индекс символа
        last_seen[char] = i

    # Возвращаем подстроку с максимальной длиной
    return max_substring

print(longest_substring("prrker"))  # Вывод: "rke"

