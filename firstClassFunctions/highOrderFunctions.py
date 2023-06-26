from functools import reduce
from operator import add

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']


def reverse(word):
    return word[::-1]


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(sorted(fruits, key=len))
    print(sorted(fruits, key=reverse))
    print(sorted(fruits, key=lambda word: word[::-1]))

    print(list(map(factorial, range(10))))
    print([factorial(n) for n in range(10)])

    print(list(map(factorial, filter(lambda n: n % 2 == 0, range(10)))))
    print([factorial(n) for n in range(10) if n % 2 == 0])

    print(reduce(add, range(100)))
    print(sum(range(100)))
