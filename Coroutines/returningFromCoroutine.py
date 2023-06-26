from collections import namedtuple
from inspect import getgeneratorstate

Result = namedtuple('Result', 'avg count')


def averager():
    total = 0
    cnt = 0
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1

    return Result(total / cnt, cnt)


if __name__ == '__main__':
    coro = averager()
    next(coro)
    coro.send(100)
    coro.send(200)
    coro.send(300)
    try:
        res = coro.send(None)
    except StopIteration as ex:
        res = ex.value
        print(res)
    print(getgeneratorstate(coro))
