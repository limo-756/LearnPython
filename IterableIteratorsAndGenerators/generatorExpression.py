import re
import reprlib


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


if __name__ == '__main__':
    res1 = [x * 3 for x in gen_AB()]
    print(res1)

    for i in res1:
        print('--> ', i)

    res2 = (x * 3 for x in gen_AB())
    print(res2)
    for i in res2:
        print('--> ', i)
