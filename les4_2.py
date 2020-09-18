from statistics import mean as mn, median as md
from itertools import cycle
import time
import random
import sys
import functools

a = [itm for itm in range(2, 1000, 3) if itm & 1]


def my_sum(x, y):
    return x + y


def my_pow(x, y):
    return x ** y


def statistics():
    return 0


proc = {
    'sum': my_sum,
    'pow': my_pow
}

print(sys.argv)
if len(sys.argv) > 3:
    _, f, x, y = sys.argv  # 'sum'

    print(proc[f](float(x), float(y)))

tmp = ['one', 'two', 'three', 'four', 'five']


# for itm in cycle(range(10)):
#     print(itm)
#     time.sleep(1.5)
#     num = random.choice(tmp)
#     print(num)

def my_s(*args):
    return args[-1] + my_s(*args[:-1]) if args else 0


print(my_s(7))
