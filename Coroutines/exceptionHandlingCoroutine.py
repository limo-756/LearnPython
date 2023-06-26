from inspect import getgeneratorstate

class DemoException(Exception):
    """An exception type for demo"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
            x = x + 10
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> couroutine received: {!r}'.format(x))
    print("is it unreachable?")
    raise RuntimeError('This line should never run.')


def demo_finally():
    print('-> finally coroutine started')
    try:
        while True:
            try:
                x = yield
                x = x + 10
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> couroutine received: {!r}'.format(x))
    finally:
        print("-> coroutine ending!")


if __name__ == '__main__':

    # normal execution termination with close method
    coro = demo_exc_handling()
    next(coro)
    coro.send(100)
    coro.send(122)
    print(getgeneratorstate(coro))
    coro.send(143)
    coro.close()
    print(getgeneratorstate(coro))

    # DemoException handling
    print("DemoException example")
    demo = demo_exc_handling()
    next(demo)
    demo.send(100)
    demo.send(122)
    print(getgeneratorstate(demo))
    demo.throw(DemoException)
    print(getgeneratorstate(demo))

    # Unhandled exception terminates the coroutine
    print("UnHandled exception example")
    un_handled_exception = demo_exc_handling()
    next(un_handled_exception)
    un_handled_exception.send(100)
    un_handled_exception.send(122)
    print(getgeneratorstate(un_handled_exception))
    try:
        un_handled_exception.throw(RuntimeError)
    except RuntimeError as ex:
        print(ex)
        print(getgeneratorstate(un_handled_exception))

    # finally example (How to hv cleanup irrespective of exception)
    print("finally example")
    un_handled_exception = demo_finally()
    next(un_handled_exception)
    un_handled_exception.send(100)
    un_handled_exception.send(122)
    print(getgeneratorstate(un_handled_exception))
    try:
        un_handled_exception.throw(RuntimeError)
    except RuntimeError as ex:
        print(ex)
        print(getgeneratorstate(un_handled_exception))

