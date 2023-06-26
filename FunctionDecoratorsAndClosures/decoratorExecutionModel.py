registry = []


def register(func):
    print("Registering function(%s)" % func)
    registry.append(func)
    return func


@register
def f1():
    print("You are in f1")


@register
def f2():
    print("You are in f2")


def f3():
    print("You are in f3")


if __name__ == '__main__':
    print("Starting main")
    print("registry -> ", registry)
    f1()
    f2()
    f3()
