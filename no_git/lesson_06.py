# file_1 = open('hello.txt', 'r', encoding='utf-8')
# file_1 = open('../lesson_06/hello.txt', 'r', encoding='utf-8')
# print('Проверка')
# content = file_1.read()
# print(content)
# file_1.close()
txt = '''Пробуем записать в файл текст.
Используем метод .write().'''
with open('write_method.txt', 'w', encoding='utf-8') as f:
    f.write(txt)

txt_lines = ['Пробуем записать в файл текст.\n',
'Используем метод .writelines().']
with open('writelines_method.txt', 'w', encoding='utf-8') as f:
    f.writelines(txt_lines)

txt = '''Пробуем дозаписать в файл текст.
Режим доступа "a"'''
with open('append_text.txt', 'a', encoding='utf-8') as f:
    f.write(txt)