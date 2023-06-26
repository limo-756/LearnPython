import re
import reprlib
from collections import abc


class Sentence:
    RE_WORD = re.compile('\w+')

    def __init__(self, text):
        self.text = text
        self.words = self.RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:

    def __init__(self, words) -> None:
        super().__init__()
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == '__main__':
    print(issubclass(Sentence, abc.Iterator))
    print(isinstance(Sentence(''), abc.Iterator))
