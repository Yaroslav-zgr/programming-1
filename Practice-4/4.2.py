def permute(nums):
    # Если список пуст, возвращаем пустой список
    if not nums:
        return []

    # Если в списке только один элемент, возвращаем список с этим элементом
    if len(nums) == 1:
        return [nums]

    # Инициализация списка для хранения всех перестановок
    permutations = []

    # Перебор каждого элемента
    for i in range(len(nums)):
        # Исключение текущего элемента
        rest = nums[:i] + nums[i+1:]
        # Генерация всех перестановок для оставшихся элементов
        for p in permute(rest):
            # Добавление текущего элемента к каждой перестановке
            permutations.append([nums[i]] + p)

    # Удаление дубликатов
    unique_permutations = [list(x) for x in set(tuple(x) for x in permutations)]

    # Возвращение списка всех уникальных перестановок
    return unique_permutations

# Пример использования функции
nums = [1,2,3] # Вводим [1,2,3]
print(permute(nums)) # Результат: [[1, 3, 2], [1, 2, 3], [2, 1, 3], [3, 2, 1], [3, 1, 2], [2, 3, 1]]
