import re

WORD_RE = re.compile('\w+')

index = {}


def ugly_way():
    occurrence = index.get(word, [])
    occurrence.append(location)
    index[word] = occurrence


def good_way():
    index.setdefault(word, []).append(location)


if __name__ == '__main__':
    with open('../output/text.txt', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                good_way()

    for word in sorted(index, key=str.upper):
        print(word, index[word])
