# Усложнение [две звездочки]:
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих
# чисел. Например:
#
#
# gen1 = iterator_with_yield(14)
# next(gen1)
# (1, 1)
# next(gen1)
# (3, 4)
# next(gen1)
# (5, 9)
# next(gen1)
# (7, 16)
# next(gen1)
# (9, 25)
# next(gen1)
# (11, 36)
# next(gen1)
# (13, 49)
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration


# Вариант 1, если вычислять сумму мы должны сами
#
#
# def iterator_with_yield(n):
#     for gen_step in range(1, n + 1, 2):
#         yield gen_step
#
#
# n = int(input('n: '))
# gen = iterator_with_yield(n)
# sum_gen = 0
# while True:
#     current_number = next(gen)
#     sum_gen += current_number
#     print(f'({current_number}, {sum_gen})')


# Вариант 2, если сумму надо посчитать в функции.

def iterator_with_yield(n):
    sum_gen = 0
    for gen_step in range(1, n + 1, 2):
        sum_gen += gen_step
        yield gen_step, sum_gen


n = int(input('n: '))
gen = iterator_with_yield(n)

while True:
    print(next(gen))