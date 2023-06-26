def deco(func):
    def inner():
        print("Running Inner() function")

    return inner


@deco
def target():
    print("Running target() function")


if __name__ == '__main__':
    target()
    print(target)
