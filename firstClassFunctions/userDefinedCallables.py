import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('empty collection')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    print(list(map(callable, [str, abs, 123])))
    l = [10, 20, 30, 40, 50]
    bingo = BingoCage(l)
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))
    print(dir(bingo))
