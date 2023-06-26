def fact(n):
    """This function calculate factorial of a number"""
    return 1 if n < 2 else n * fact(n - 1)


if __name__ == '__main__':
    print("factorial of 42 : ", fact(42))
    print(fact.__doc__)
    print(fact)
    print(type(fact))
    print(help(fact))

    factorial = fact
    print(factorial.__doc__)
    print(factorial)
    print(type(factorial))

    print(map(fact, range(10)))
    print(list(map(fact, range(10))))
    print(dir(fact))
