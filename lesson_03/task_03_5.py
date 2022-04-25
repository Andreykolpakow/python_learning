# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх заданных списков.
# Условие задачи
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Техническое задание
#
# Функция должна вернуть список строк-шуток.
# Функция принимает 4 параметра: количество шуток и 3 списка со словами.
# В списках nouns, adverbs, adjectives не обязательно одинакое количество элементов. Они могут быть произвольной
# длины.
# Проверьте работу функции для количества шуток больше, чем длины списков слов и меньше.
# Сделайте вызов функции как с позиционными аргументами, так и с именованными.
# Менять исходные списки nouns, adverbs, adjectives нельзя. Это «side effects»
# Документируйте код функции.
# Примеры/Тесты:
#
#
# >>> get_jokes(3, nouns, adverbs, adjectives)
# ['автомобиль ночью мягкий', 'лес сегодня утопичный', 'дом вчера зеленый']
# >>> get_jokes(5, nouns, adverbs, adjectives)
# ['автомобиль вчера зеленый',
#  'дом ночью мягкий',
#  'огонь ночью утопичный',
#  'дом позавчера зеленый',
#  'город вчера утопичный']
# >>>
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number, list_1, list_2, list_3):
    """Make jokes and bring them back"""
    result_list = []
    for i in range(number):
        result_list.append(f'{random.choice(list_1)} {random.choice(list_2)} '
                           f'{random.choice(list_3)}')
    return result_list


wish_list = get_jokes(3, nouns, adverbs, adjectives)
wish_list_named = get_jokes(list_1=nouns, number=7, list_3=adjectives, list_2=adverbs)
print(wish_list)
for i  in range(len(wish_list_named)):
    print(f"'{wish_list_named[i]}'")