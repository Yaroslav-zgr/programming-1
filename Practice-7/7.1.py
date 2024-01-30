def santa_users(users):
    # Инициализация пустого словаря
    user_dict = {}

    # Цикл по каждому пользователю в списке
    for user in users:
        # Если у пользователя есть почтовый индекс, добавить его в словарь
        if len(user) == 2:
            user_dict[user[0]] = user[1]
        # Если у пользователя нет почтового индекса, добавить None в словарь
        else:
            user_dict[user[0]] = None

    # Вернуть словарь
    return user_dict

# Пример использования функции
users = [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]
print(santa_users(users))
