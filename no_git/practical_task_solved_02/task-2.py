# 2.Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
#  (добавить кавычку до и кавычку после элемента списка, являющегося числом)
#  и дополнить нулём до двух целочисленных разрядов:
# Результат:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
#
# *Примечание:*
# - Задача обычной сложности: создайте новый список и заполните его нужными значениями, включая элементы-кавычки
#       или измените существующий список, но не добавляйте элементы-кавычки.
# - * Задача повышенной сложности: измените существующий список, и добавьте элементы-кавычки.
#       Эта задача намного серьезнее, чем может сначала показаться.
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Вывести список и строку на экран.

#lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#lst = ['примерно в', '23', 'часа', '8', 'минут', '03', '05', 'секунд', 'температура', 'воздуха', 'была', '5', 'градусов Цельсия', 'темп','воды','+2.0','градусов','Цельсия' ,'-2']
lst = ['+9', 'примерно в', '23', 'часа', '8', 'минут', '03', '05', 'секунд', 'температура', 'воздуха', 'была', '5', 'градусов Цельсия', 'темп','воды','+2.0','градусов','Цельсия' ,'-2', '11']

print(f"Исходный список:\n{lst}")
# Копии списков нужны т.к. несколько раз разными алгоритмами меняем список in place
lst_copy1 = lst.copy()
lst_copy2= lst.copy()
#  Обычная сложность: Решение через формирование нового списка + элементы-кавычки
lst_new1 = []
for el in lst:
    check_digit_1 = el.isdigit()
    check_digit_2 = (el[0] == "+" or el[0] == "-") and el[1:].isdigit()
    if check_digit_1 or check_digit_2:
        if len(el) == 1:
            el = f"0{el}"
        elif check_digit_2 and len(el[1:]) == 1:
            el = f"{el[0]}0{el[1:]}"
        lst_new1.append('"')
        lst_new1.append(el)
        lst_new1.append('"')
    else:
        lst_new1.append(el)

#  Обычная сложность: Решение через изменение in place существующего списка, без элементов-кавычек
for idx, el in enumerate(lst_copy1):
    check_digit_1 = el.isdigit()
    check_digit_2 = (el[0] == "+" or el[0] == "-") and el[1:].isdigit()
    if check_digit_1 or check_digit_2:
        if len(el) == 1:
            el = f"0{el}"
        elif check_digit_2 and len(el[1:]) == 1:
            el = f"{el[0]}0{el[1:]}"
        lst_copy1[idx] = f'"{el}"'

# Задача повышенной сложности: измените существующий список, и добавьте элементы-кавычки.
# Эта задача намного серьезнее, чем может сначала показаться.
# Вставляя в существующий список новые элементы(метод списка .insert()), мы сдвигаем остальные элементы вправо (по индексам)
# Т.е. после вставки нового элемента индексы последующих элементов ИЗМЕНЯТСЯ
# Это можно явно учитывать дополнительным счетчиком
# А можно идти по списку с конца к началу, тогда сдвиг элементов не будет мешать
idx_insert = len(lst)-1
for idx in range(len(lst_copy2)-1, -1, -1):
    el = lst_copy2[idx]
    # Проверка на число в требуемом формате.
    check_digit_1 = el.isdigit()
    check_digit_2 = (el[0] == "+" or el[0] == "-") and el[1:].isdigit()
    if check_digit_1 or check_digit_2:
        if len(el) == 1:
            el = f"0{el}"
        elif check_digit_2 and len(el[1:]) == 1:
            el = f"{el[0]}0{el[1:]}"
        lst_copy2.insert(idx+1, '"')
        lst_copy2[idx] = el
        lst_copy2.insert(idx, '"')


print(f"Новый список+добавление элементов:\n{lst_new1}")
print(f"In place изменение без добавление элементов:\n{lst_copy1}")
print(f"In place изменение+добавление элементов:\n{lst_copy2}")

# Для lst_copy1 - элементарно
rez_new1 = ""
for idx,el in enumerate(lst_copy1):
    rez_new1 += f"{el} "
print(rez_new1)

# Для lst_new1 и lst_copy2 - одинаково, но надо избежать лишних пробелов около кавычек
rez_new2 = ""
for idx in range(len(lst_new1)-1):
    el_c = lst_new1[idx]
    el_n = lst_new1[idx+1]
    # Формирование условия: элемент - число после нашей обработки
    check_if_current_number = el_c.isdigit() or (el_c[0] in ("+", "-") and el_c[1:].isdigit())
    check_if_next_number = el_n.isdigit() or (el_n[0] in ("+", "-") and el_n[1:].isdigit())
    if (el_c == '"' and check_if_next_number) or check_if_current_number :
        rez_new2 += f"{el_c}"
    else:
        rez_new2 += f"{el_c} "
rez_new2 += f"{lst_new1[-1]}"


####    check_first_quotes = el == '"' and idx >= 1 and not lst_new1[idx-1][-1].isdigit()
##    if el[-1].isdigit() or check_first_quotes :
##        rez_new2 += f"{el}"
##    else:
##        rez_new2 += f"{el} "
print()
print(rez_new2)


