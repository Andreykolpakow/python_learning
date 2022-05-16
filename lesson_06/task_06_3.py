# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Загрузить данные из обоих файлов и сформировать словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в текстовый файл. Проверить сохранённые данные.

# Техническое задание
#
# Данные файлов синхронизированы построчно: 1-ой строке файла с ФИО соответствует 1-ая строка файла с хобби и т.п.
# При хранении данных используется принцип: одна строка — один пользователь.
# Разделитель между значениями — запятая. Не используем пакеты для парсинга CSV файлов. При формировании словаря -
# хобби следует разделить символом «точка с запятой».
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся ФИО использовать вместо
# хобби None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Вы можете использовать здесь функции zip и zip_longest, но лучше обойтись без них.

# Усложнение:
#
# Выполните запись результирующего словаря в файл json формата. Сделайте так чтобы русские букву читались как обычный
# текст, без преобразования в коды unicode.

# Примеры/Тесты:
#
# Фрагмент файла с данными о пользователях (task_3_users.csv):
#
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Сидоров,Сидор,Сидорович
#
# Фрагмент файла с данными о хобби (task_3_hobby.csv):
#
#
# скалолазание,охота
# горные лыжи
# вышивание крестиком, бои без правил
#
# Фрагмент результирующего файла (task_3_rezult.txt):
#
#
# {'ИИИ': 'скалолазание;охота', 'ППП': 'горные лыжи', 'ССС': 'вышивание крестиком; бои без правил'}

import os.path
import json

res_dict = {}


with open('task_3/task_3_users.csv', 'r', encoding='utf-8') as users:
    with open('task_3/task_3_hobby.csv', 'r', encoding='utf-8') as hobbyes:

        users_list = users.readlines()
        hobbyes_list = hobbyes.read().splitlines()
        for i in range(len(hobbyes_list)):
            hobbyes_list[i] = hobbyes_list[i].replace(',', ';')

        fio_list = []
        for user in users_list:
            fio = ''
            fio_full = user.split(',')
            for name in fio_full:
                fio += (name[:1])
            fio_list.append(fio)

        if len(fio_list) > len(hobbyes_list):
            for i in range(len(fio_list)):
                while i < len(hobbyes_list):
                    res_dict[fio_list[i]] = hobbyes_list[i]
                    i += 1
                res_dict[fio_list[i]] = None
        elif len(fio_list) < len(hobbyes_list):
            while i < len(fio_list):
                res_dict[fio_list[i]] = hobbyes_list[i]
                i += 1
            exit(1)
        elif len(fio_list) == len(hobbyes_list):
            for i in range(len(fio_list)):
                res_dict[fio_list[i]] = hobbyes_list[i]
        else:
            print('Такого не может быть. Проверь условия')

        with open('res_file.txt', 'w', encoding='utf-8') as f:
            res_dict_str = json.dumps(res_dict, ensure_ascii=False)
            f.write(res_dict_str)

        with open('res_file.json', 'w', encoding='utf-8') as f:
            json.dump(res_dict, f, ensure_ascii=False)










        # print(res_dict)
