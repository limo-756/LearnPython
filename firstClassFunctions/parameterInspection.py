from inspect import signature


def fun(a, b, c, *d, e=None, **f):
    g = "Hello"
    h = 10.23
    print(a, b, c, d, e, f, g, h)


if __name__ == '__main__':
    sig = signature(fun)
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, ' = ', param.default)
        print(param.annotation)
