from inspect import getgeneratorstate

def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)
    yield 10
    z = yield


def simple_coro2(a):
    print('-> Started: a = ', a)
    b = yield a
    print('-> Received: b = ', b)

    c = yield a + b
    print('-> Received: c =', c)


if __name__ == '__main__':
    coro = simple_coroutine()

    # coro.send(100)
    # TypeError: can't send non-None value to a just-started generator

    print("Obj : ", coro)
    next(coro)
    print("Obj : ", coro)
    print(coro.send(42))
    print("Obj : ", coro)
    print(next(coro))

    print("#########")
    coro2 = simple_coro2(14)
    print(getgeneratorstate(coro2))
    print(next(coro2))
    print(getgeneratorstate(coro2))
    print(coro2.send(28))
    try:
        print(coro2.send(99))
    except StopIteration:
        pass
    print(getgeneratorstate(coro2))



