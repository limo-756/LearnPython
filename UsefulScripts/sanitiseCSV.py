import logging
import pandas as pd
import csv
import codecs

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    # open CSV
    header_row = ['reserved_keywords']
    write_file = open("/Users/anurag.sh/workspace/sanitised_influencer_2.csv", 'w')
    csv_writer = csv.writer(write_file)
    csv_writer.writerow(header_row)

    with open('/Users/anurag.sh/workspace/influencer2.csv') as file:
        # Then for each orderId fetch userId and HostingServer
        reader = csv.reader(file)
        for i, line in enumerate(reader):
            if i > 0:
                print(i)
                sanitised_word = sanitize(line[0])
                if len(sanitised_word) > 0:
                    csv_writer.writerow([sanitised_word])


def sanitize(word):
    new_word = ""
    for c in word:
        if is_a_char(c) or is_a_digit(c) or c == '.':
            new_word = new_word + c
    return new_word.lower()


def is_a_char(ch):
    return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')


def is_a_digit(ch):
    return '0' <= ch <= '9'


if __name__ == '__main__':
    main()
