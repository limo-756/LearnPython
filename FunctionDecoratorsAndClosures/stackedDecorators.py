def f1(func):
    print("You are in f1")
    return func


def f2(func):
    print("You are in f2")
    return func


@f1
@f2
def f():
    print("You are in f")


if __name__ == '__main__':
    f()
