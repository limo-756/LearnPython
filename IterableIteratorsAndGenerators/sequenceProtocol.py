import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


class Foo:

    def __iter__(self):
        pass


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)

    print(list(s))
    print(issubclass(Sentence, abc.Iterable))
    print(isinstance(Sentence(''), abc.Iterable))

    print("Foo class ===>")
    print(issubclass(Foo, abc.Iterable))
    print(isinstance(Foo(), abc.Iterable))
