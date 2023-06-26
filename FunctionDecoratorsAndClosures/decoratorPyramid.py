import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result

        return clocked

    return decorate


@clock()
def f1(message):
    print('This is f1 ', message)


@clock()
def snooze(seconds):
    time.sleep(seconds)

@clock('{name} {elapsed}s')
def snooze1(seconds):
    time.sleep(seconds)


@clock('{name}({args}) dt={elapsed:0.3f}s')
def snooze2(seconds):
    time.sleep(seconds)


if __name__ == '__main__':

    f1('ABCD')

    for i in range(3):
        snooze(.123)

    for i in range(3):
        snooze1(.123)

    for i in range(3):
        snooze2(.123)
