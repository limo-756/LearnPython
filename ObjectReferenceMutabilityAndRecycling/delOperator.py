import weakref


def bye():
    print('S1 is going for deletion')


if __name__ == '__main__':
    s1 = {1, 2, 3}
    s2 = s1
    ender = weakref.finalize(s1, bye)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = "a different obj"
    print(ender.alive)
