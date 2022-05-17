# Усложнение [одна звездочка]:
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно), для
# чисел, квадрат которых меньше 200.


def iterator_with_yield(n):
    for gen_step in range(1, n + 1, 2):
        if gen_step ** 2 < 200:
            yield gen_step


n = int(input('n: '))
gen = iterator_with_yield(n)

while True:
    next(gen)
    # print(next(gen)) # Для проверки работы генератора. Включать врозь с предыдущим next