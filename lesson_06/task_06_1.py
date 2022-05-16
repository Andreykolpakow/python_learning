# 1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Техническое задание
#
# Не использовать библиотеки для парсинга. Только работа со строками.
# Создать список кортежей вида: '(<remote_addr>, <request_type>, <requested_resource>)'. Именно список кортежей.
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Вывести список на экран.
# Формат вывода результата:
#
#
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_1'),
#     ...
# ]
#
# Примечание:
#
# Файл логов можно загрузить отсюда: https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs



import os.path

# file_path = os.path.join('.', 'data_for_practice', 'nginx_logs.txt') # почему-то подстановка
# такого file_path в open вызывала ошибку File Not Found

log_file = open('data_for_practice/nginx_logs.txt', 'r', encoding='utf-8')
result_list = []

for line in log_file:
    remote_addr, _, _, _, _, request_type, requested_resource, *_ = line.split()
    request_type = request_type[1:]
    added_tuple = (remote_addr, request_type, requested_resource)
    result_list.append(added_tuple)

print('[', *result_list, ']', sep='\n')


log_file.close()