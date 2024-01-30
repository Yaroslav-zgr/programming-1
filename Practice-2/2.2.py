def reverse_words(s):
    # Разбиваем строку на слова
    words = s.split()

    # Переворачиваем порядок слов
    words = words[::-1]

    # Преобразуем первое слово к заглавным буквам, а остальные - к строчным
    for i in range(len(words)):
        if i == 0:
            words[i] = words[i].capitalize()
        else:
            words[i] = words[i].lower()

    # Объединяем слова обратно в строку с одним пробелом между словами
    result = ' '.join(words)

    # Возвращаем результат
    return result

print(reverse_words("пРивет мИР"))  # Вывод: "Мир привет"
