# homework lesson: 3, task:3

"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    return max(a + b, b + c, c + a)


def my_func2(a, b, c):
    return sum((a, b, c)) - min(a, b, c)


# можно lambda
my_func3 = lambda a, b, c: sum((a, b, c)) - min((a, b, c))

assert my_func(1, 2, 3) == 5, 'my_func(1, 2, 3)'
assert my_func(2, 7, 0) == 9, 'my_func(2, 7, 0)'
assert my_func(5, 9, 22) == 31, 'my_func(5, 9, 22)'
assert my_func(-22, 3, 7) == 10, 'my_func(-22, 3, 7)'

assert my_func2(1, 2, 3) == 5, 'my_func2(1, 2, 3)'
assert my_func2(2, 7, 0) == 9, 'my_func2(2, 7, 0)'
assert my_func2(5, 9, 22) == 31, 'my_func2(5, 9, 22)'
assert my_func2(-22, 3, 7) == 10, 'my_func2(-22, 3, 7)'
