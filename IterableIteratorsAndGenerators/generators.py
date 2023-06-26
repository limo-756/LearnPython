import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text) -> None:
        super().__init__()
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word


def gen_123():
    yield 1
    yield 2
    yield 3


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


if __name__ == '__main__':
    print(gen_123)
    print(gen_123())

    for i in gen_123():
        print(i)

    g = gen_123()
    while True:
        try:
            print(next(g))
        except StopIteration:
            break

    for c in gen_AB():
        print('-->', c)
