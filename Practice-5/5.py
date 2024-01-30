def rob_banks(banks):
    # Инициализируем переменные для хранения текущего и предыдущего максимального набора
    current_max = prev_max = 0
    current_banks = prev_banks = []

    # Для каждого банка в списке
    for i, bank in enumerate(banks):
        # Вычисляем новый максимум и соответствующий набор банков
        new_max = max(prev_max + bank[1], current_max)
        new_banks = prev_banks + [bank] if prev_max + bank[1] > current_max else current_banks[:]

        # Обновляем предыдущий и текущий максимумы и наборы банков
        prev_max, current_max = current_max, new_max
        prev_banks, current_banks = current_banks, new_banks

    # Возвращаем максимальную сумму и соответствующий набор банков
    return current_max, [(bank[0], i+1) for i, bank in enumerate(current_banks)]

# Тестовые случаи
print(rob_banks([("sber",10),("Tin",5),("Vol",6),("Ker",12)]))   # Результат: (22, [("sber",1),("Ker",4)])
