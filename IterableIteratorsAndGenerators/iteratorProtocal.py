from abc import abstractmethod
from collections.abc import Iterable
import IterableIteratorsAndGenerators.sequenceProtocol


class Iterator(Iterable):
    __slots__ = ()

    @abstractmethod
    def __next__(self):
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasscheck__(cls, C):
        if cls is Iterator:
            if (any("__next__" in B.__dict__ for B in C.__mro__)
                    and any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
        return NotImplemented


if __name__ == '__main__':
    s3 = IterableIteratorsAndGenerators.sequenceProtocol.Sentence('Pig and pepper')
    it = iter(s3)
    print(it)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

    print(list(it))
    print(list(iter(s3)))

