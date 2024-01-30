def analyze_lists(list1, list2):
    # Преобразование списков в множества для удаления дубликатов и упрощения операций
    set1 = set(list1)
    set2 = set(list2)

    # Нахождение пересечения множеств (элементы, присутствующие в обоих списках)
    common = set1 & set2

    # Нахождение элементов, присутствующих только в одном списке
    unique = (set1 - set2) | (set2 - set1)

    # Нахождение оставшихся элементов в list1 после извлечения элементов из list2
    remaining_in_list1 = set1 - set2

    # Нахождение оставшихся элементов в list2 после извлечения элементов из list1
    remaining_in_list2 = set2 - set1

    # Возвращение результатов
    return len(common), len(unique), len(remaining_in_list1), len(remaining_in_list2)

# Пример использования функции
list1 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25]
list2 = [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
print(analyze_lists(list1, list2))
