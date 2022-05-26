# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Выводит или не выводить первый элемент - решите сами. Используйте генераторы или генераторные выражения.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

src = [300, 2000, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {src}")
lst1 = [src[idx] for idx in range(1, len(src)) if src[idx] > src[idx-1]]
print(lst1)
# Оригинальное решение, но надо проверять его эффективность по времени. Тут zip
lst2 = [next for prev, next in zip(src, src[1:]) if next > prev]
print(lst2)


# 5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
# Используйте генераторы или генераторные выражения.
# Сначала найдите способ определить уникальность элемента в списке. Подумайте о сохранении порядка исходного списка.

# Решешение "в лоб" через список. Неээфективно, но просто
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"Исходный список: {src}")
# [23, 1, 3, 10, 4, 11]
print([num for num in src if src.count(num) == 1])

# Решение как в методичке. Разберитесь сами, зачем здесь два множества.
unique = set()
already_view = set()
for el in src:
    if el not in already_view:
        unique.add(el)
    else:
        unique.discard(el)
    already_view.add(el)
# Тут восстанавливаем порядок исходного списка
unique_list = [el for el in src if el in unique]
print(unique_list)
