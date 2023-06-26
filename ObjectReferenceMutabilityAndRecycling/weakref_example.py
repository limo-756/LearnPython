import weakref

if __name__ == '__main__':
    a_set = {1, 0}
    ref1 = weakref.ref(a_set)
    print(ref1)
    print(ref1())
    a_set = {2, 4}
    print(ref1() is None)
    print(ref1() is None)
