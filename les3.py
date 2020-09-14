from typing import Callable, Iterable, List

"""
map
zip
round
sum
filter
min
max
abs
sort
reduce
"""


def my_map(func: Callable, some: Iterable) -> list:
    """
    Реализация функции map
    :param func: call object
    :param some: iterable object
    :return: list result
    """
    result = []
    for itm in some:
        result.append(func(itm))
    return result


some = ['1', '2']


def some_append(itm) -> list:
    some = []
    some.append(itm)
    return some


def some_f(*args, **kwargs):
    print(type(kwargs))
    print(type(args))
    print(args)
    print(kwargs)


def my_min(*args, key=lambda x: x):
    result = float('inf')
    for itm in args:
        if result > key(itm):
            result = key(itm)
    return result


some_f(1, 2, 3, 4, 5, key=1, key2=33, key3=44)

a = [1, 2, 3, 4, 5]


def some_key(x):
    return x + 22 ** 2


def some_temp(template: tuple):
    def producter(items):
        product = {}
        for name, item in zip(template, items):
            product[name] = item
        return product

    return producter


producter_1 = some_temp(('название', 'колличество'))
a = producter_1(('comp', 22))
print(a)

# print(my_min(333, 444, 666, 22, key=lambda x: x + 22 ** 2))
#
#
# b = some_append('HELLO')
# print(some)
# print(b)

# b = my_map(str, a)
# c = my_map(some=a, func=str)
