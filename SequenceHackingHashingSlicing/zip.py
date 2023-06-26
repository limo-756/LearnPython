from itertools import zip_longest

if __name__ == '__main__':
    print(zip(range(3), 'ABC'))
    print(tuple(zip(range(3), 'ABC')))
    print(list(zip(range(3), 'ABC', [0.0, 0.1, 0.2, 0.3])))
    print(list(zip_longest(range(3), 'ABC', [0.0, 0.1, 0.2, 0.3], fillvalue=None)))