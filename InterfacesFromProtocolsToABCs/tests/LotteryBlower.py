import InterfacesFromProtocolsToABCs.tests.Tombola
import random


class LotteryBlower(InterfacesFromProtocolsToABCs.tests.Tombola):

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
