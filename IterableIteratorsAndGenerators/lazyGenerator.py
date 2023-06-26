import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text) -> None:
        super().__init__()
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # for match in RE_WORD.finditer(self.text):
        #     yield match.group()
        return (match.group() for match in RE_WORD.finditer(self.text))


if __name__ == '__main__':
    s = Sentence('This is lazy impl')
    print(s)
    print(iter(s))
    print(list(s))
