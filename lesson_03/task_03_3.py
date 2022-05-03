# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую
# словарь, в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с
# соответствующей буквы.
# Условие задачи
# Техническое задание
#
# Количество передаваемых имен в функцию может быть любым. Считаем, что переданы будут только корректные строки.
# Обратите внимание, что функция принимает произвольное количество параметров.
# Вернуть словарь с ключами, отсортированными в алфавитном порядке.
# Выполнить вызов функции для списка имен и вывести на экран словарь.
# Вы можете вывести на экран «красиво» - как в примере на каждой строке одна буква и список, но это не обязательно.
# Примеры/Тесты:
#
#
# >>> thesaurus("Иван", "Мария", "Петр", "Илья", "Артем", "Вадим", "Анатолий")
# {
#     "А": ["Артем", "Анатолий"],
#     "В": ["Вадим"],
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }


def thesaurus(*args):
    names = (args)
    result_dict = {}
    first_symbols = []
    for name in names:
        first_symbols.append(name[0])
    first_symbols_set = set(first_symbols)
    first_symbols = list(first_symbols_set)
    first_symbols.sort()
    for first_symbol in first_symbols:
        litera = []
        for name in names:
            if first_symbol == name[0]:
                litera.append(name)
        result_dict[first_symbol] = litera
    # sorted(result_dict.keys())
    return result_dict


result_dict_global = thesaurus('Leo', 'Joe', 'Max', 'Kate', 'Kirill', 'John', 'Mary', 'Андрей', 'Маша', 'Алексей')
print(result_dict_global) # Вывел результат одной строкой
for k, v in result_dict_global.items(): # Вывел построчно
    print(f'"{k}": {v}')