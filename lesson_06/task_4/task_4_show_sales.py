# Вывод на экран записей:
# Имя исполняемого скрипта: task_4_show_sales.py
# Предполагаем, что первая запись имеет номер 1.
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи от номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная от номера, равного первому числу, по номер,
# равный второму числу, включительно; Если второе число больше, чем количество записей в файле - просто
# выводить до конца.
# Корректно обработать неправильное количество или тип переданных параметров.
# Примеры/Тесты:
# Примеры запуска скриптов:
#
#
# python add_sale.py 5978
# python add_sale.py 891
# python add_sale.py 7879
# python add_sale.py 1573
# python show_sales.py
# 5978
# 891
# 7879
# 1573
# python show_sales.py 3
# 7879
# 1573
# python show_sales.py 1 3
# 5978
# 891
# 7879
#
# Усложнение Подумать, как избежать чтения всего файла в память при реализации чтения данных в пунктах 4 и 5.

import sys

arg_list = (sys.argv)
# print(arg_list) #чтобы при отладке всегда видеть, какие аргументы получены

if len(arg_list) > 3:
    print('Введены лишние аргументы')
elif len(arg_list) == 3:
    if arg_list[1].isdigit() and arg_list[2].isdigit():
        start, end = int(arg_list[1]), int(arg_list[2])
        if start <= end:
            with open('bakery.csv', 'r', encoding='utf-8') as f:
                for i in range(end):
                    for line in f:
                        i += 1
                        if start <= i <= end:
                            print(line, end='')
        else:
            print('Уточните данные')
    else:
        print('Введите числа')
elif len(arg_list) == 2:
    if arg_list[1].isdigit():
        start = int(arg_list[1])
        i = 0
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for line in f:
                i += 1
                if i < start:
                    continue
                print(line, end='')
    else:
        print('Уточните данные')
else:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')





