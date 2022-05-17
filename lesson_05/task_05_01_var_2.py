# Усложнение [одна звездочка]:
# нужен генератор нечётных чисел от 1 до n (включительно), для чисел, квадрат которых меньше 200. Все
# остальное как в основном задании.


def iterator_without_yield(n):
    gen1 = (n for n in range(1, n + 1, 2) if n ** 2 < 200)
    return gen1


n = int(input('n: '))
gen = iterator_without_yield(n)
while True:
    next(gen)
    # print(next(gen))
