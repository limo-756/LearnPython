def f(a, b):
    a += b
    return a


if __name__ == '__main__':
    x = 1
    y = 2
    print(f(x, y), x, y)

    a = [1, 2]
    b = [3, 4]
    print(f(a, b), a, b)

    t = (10, 20)
    u = (30, 40)
    print(f(t, u), t, u)
