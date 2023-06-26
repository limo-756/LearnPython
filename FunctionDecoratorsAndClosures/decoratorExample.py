import time


def clock(func):
    def clocked(*args):
        t0 = time.clock_gettime_ns(0)
        result = func(*args)
        elapsed = time.clock_gettime_ns(0) - t0
        name = func.__name__
        arg_str = ' , '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'calling factorial(20)')
    print('20 !', factorial(20))