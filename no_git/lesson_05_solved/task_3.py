# Есть два списка: tutors - имена учеников, groups - названия их классов.
# Например:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена']
# groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
#
# Необходимо реализовать генератор или функцию-генератор,
# возвращающий кортежи вида `(<tutor>, <groups>)`.
# ('Иван', '9А')
# ('Анастасия', '7В')
#
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке groups меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None), например: ('Станислав', None)
# Доказать, что вы создали именно генератор.
# Проверить его работу вплоть до истощения.


# Функция генератор
def generator_tutors(tutors, groups):
    # Достаточно важно не вычислять len(groups) внутри цикла for. Это дополнительное время на каждой итерации
    length = len(groups)
    # можно было и просто по индексам. Но индексы нужны, чтобы обратиться к другому списку
    for idx, man in enumerate(tutors):
        if idx < length:
            yield man, groups[idx]
            # yield (tutors[idx], groups[idx])  # Можно и так
        else:
            yield man, None

        # Вместо этого блока if можно написать так:
##        yield man, groups[idx] if idx < length else None


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
#groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
groups = ['9А', '7В', '9Б', '9В']

print("Использование функции-генератора\n")
print(f"Ученики: {tutors}")
print(f"Классы: {groups}")
gen_tutors = generator_tutors(tutors, groups)
print(f"Тип объекта: {type(gen_tutors)}")
print(f"Все значения генератора")
for el in gen_tutors:
    print(el)

# Т.к. использование zip запрещено условием задачи,
# то придется пройтись по индексам, а не по элементам (а было бы удобно)
#
print("\nИспользование генераторного выражения\n")
g = ((tutors[i], groups[i] if i<len(groups) else None) for i in range(len(tutors)))

for el in g:
    print(el)

