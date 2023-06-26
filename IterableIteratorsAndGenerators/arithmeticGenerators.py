from fractions import Fraction
from decimal import Decimal


class ArithmeticProgression:

    def __init__(self, begin, step, end=None) -> None:
        super().__init__()
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index
        # return (x for x in range(self.begin, ))


if __name__ == '__main__':
    print(list(ArithmeticProgression(0, 1, 3)))
    print(list(ArithmeticProgression(1, 0.5, 3)))
    print(list(ArithmeticProgression(0, 1 / 3, 1)))
    print(list(ArithmeticProgression(0, Fraction(1 / 3), 1)))
    print(list(ArithmeticProgression(0, Decimal('.1'), .3)))
