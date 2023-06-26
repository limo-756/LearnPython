registry = set()


def register(active=True):
    def decorate(func):
        print('running register(active+%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


@register(active=False)
def f1():
    print('Running f1() ')


@register()
def f2():
    print('Running f2()')


def f3():
    print('Running f3()')


if __name__ == '__main__':
    f1()
    f2()
    f3()
    print("Before adding f3 ", registry)
    register()(f3)
    print("After adding f3 ", registry)
    register(active=False)(f2)
    print("After removing f2 ", registry)
