def find_sum(N, nums, target):
    # Убедимся, что список содержит не менее 3 элементов
    if N < 3:
        return "Список должен содержать не менее 3 элементов"

    # Инициализация переменных
    closest_sum = float('inf')  # Бесконечность
    closest_nums = []

    # Перебор всех возможных комбинаций из 3 чисел
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                # Вычисление суммы текущей комбинации
                current_sum = nums[i] + nums[j] + nums[k]
                # Если текущая сумма ближе к цели, чем предыдущая ближайшая сумма
                if abs(current_sum - target) < abs(closest_sum - target):
                    # Обновление ближайшей суммы и чисел
                    closest_sum = current_sum
                    closest_nums = [nums[i], nums[j], nums[k]]

    # Возвращение ближайших чисел и их суммы
    return closest_nums, closest_sum

# Пример использования функции
N = 5
nums = [1, 2, 4, -5, -2]
target = 1
closest_nums, closest_sum = find_sum(N, nums, target)
print(closest_nums)
print(closest_sum)
