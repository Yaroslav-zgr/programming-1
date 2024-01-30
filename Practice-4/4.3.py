def group_words(words):
    # Инициализируем словарь для хранения групп слов
    groups = {}

    # Для каждого слова в списке
    for word in words:
        # Создаем ключ, состоящий из отсортированных букв слова и его длины
        key = (''.join(sorted(word)), len(word))

        # Если ключ уже есть в словаре, добавляем слово в соответствующую группу
        if key in groups:
            groups[key].append(word)
        # В противном случае создаем новую группу с этим словом
        else:
            groups[key] = [word]

    # Возвращаем все группы слов
    return list(groups.values())

# Тестовые случаи
print(group_words(["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]))   # Результат: [['qwe', 'ewq'], ['asd', 'dsa'], ['dsas'], ['qwee'], ['zxc', 'cxz'], ['xxz'], ['z'], ['s'], ['qweasdzxc'], ['zzxc']]
print(group_words(["a","a",""]))   # Результат: [['a', 'a'], ['']]
