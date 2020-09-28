import datetime as dt


def log_deco(func):

    def wrapper(*args, **kwargs):
        with open('some_log.log', 'a', encoding='UTF-8') as file:
            file.write(f'{dt.datetime.utcnow()} -- run {func.__name__}\n')
        result = func(*args, **kwargs)
        return result

    return wrapper


@log_deco
def some(x):
    return x ** 2


@log_deco
def some2(x):
    return x ** 3


if __name__ == '__main__':
    res = some(3)
    res2 = some2(4)
