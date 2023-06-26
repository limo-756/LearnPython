import re
from unicodedata import name

WORD_RE = re.compile('\w+')

words = set()

if __name__ == '__main__':
    with open('../output/text.txt', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                words.add(match.group())

    common_words = {'the', 'name', 'arguments', 'orange'}
    print(words & common_words)
    print(words.intersection(common_words))
    common_words -= words
    print(common_words)

    frozen = frozenset(range(10))
    print(frozen)

    unicodes = [chr(code) for code in range(32, 256) if 'SIGN' in name(chr(code), '')]
    print(unicodes)
