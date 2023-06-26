def f1(a):
    print(a)
    print(b)


b = 3


# def f2(a):
#     print(a)
#     print(b)
#     b = 12

def f3(a):
    print(a)
    global b
    print(b)
    b = 12


if __name__ == '__main__':
    b = 3
    f1(2)
    # f2(3)
    f3(10)
    print(b)
