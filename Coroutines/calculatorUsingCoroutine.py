from functools import wraps
from inspect import getgeneratorstate


def couroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


@couroutine
def primed_averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    avg = averager()
    next(avg)
    print(avg.send(10))
    print(avg.send(20))
    print(avg.send(70))
    avg.close()

    primed = primed_averager()
    print(getgeneratorstate(primed))
    print(primed.send(100))
    print(primed.send(134))
    print(getgeneratorstate(primed))
    print(primed.send(1654))
    primed.close()
    print(getgeneratorstate(primed))

    primed = primed_averager()
    print(getgeneratorstate(primed))
    print(primed.send(100))
    try:
        print(primed.send('asdsaf'))
    except TypeError:
        pass
    print(getgeneratorstate(primed))
    # primed.send(100)
    # StopIteration

