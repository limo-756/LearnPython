from collections import namedtuple
from inspect import getgeneratorstate

Result = namedtuple('Result', 'average count')


def averager():
    total = 0
    cnt = 0
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1

    return Result(total / cnt, cnt)


def grouper(results, key):
    while True:
        results[key] = yield from averager()


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    # print(results)
    reporter(results)


def reporter(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg':
        [49.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 46.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 41.5, 34.5, 32.4, 49.9, 50.1],
    'boys;m':
        [1.38, 1.45, 1.5, 1.23, 1.33, 1.24, 1.34, 1.21, 1.45]
}

if __name__ == '__main__':
    main(data)
