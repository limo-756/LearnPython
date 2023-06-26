import collections

if __name__ == '__main__':
    alphabet_counter = collections.Counter('abrakadabra')
    print(alphabet_counter)
    alphabet_counter.update('aaazzz')
    print(alphabet_counter)
    print(alphabet_counter.most_common(3))