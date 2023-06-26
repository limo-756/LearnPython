import abc
import random


class Tambola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """
        Adds Item from an iterable
        """

    @abc.abstractmethod
    def pick(self):
        """
        Remove item at random and return it
        This method should raise LookupError when the instance is empty
        """

    def loaded(self):
        """Returns 'True' If there's at least 1 item, 'False' otherwise."""
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class Fake(Tambola):

    def pick(self):
        return 13


class BingoCage(Tambola):

    def __init__(self, items) -> None:
        super().__init__()
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


class LotteryBlower(Tambola):

    def __init__(self, balls) -> None:
        super().__init__()
        self._balls = list(balls)

    def load(self, items):
        self._balls.extend(items)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
            return self._balls.pop(position)
        except ValueError:
            raise LookupError('pick from empty BingoCage')

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Tambola.register
class TamboList(list):

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


if __name__ == '__main__':
    # print(Fake)
    # print(Fake())
    print(issubclass(TamboList, Tambola))
    t = TamboList()
    print(isinstance(t, Tambola))

    print(Tambola.__mro__)
    print(TamboList.__mro__)
    print(BingoCage.__mro__)
