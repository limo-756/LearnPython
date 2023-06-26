import array

symbols = "$€£¥₹₿"

if __name__ == '__main__':
    print(tuple(ord(symbol) for symbol in symbols))
    print((100, (ord(symbol) for symbol in symbols)))
    print(array.array('I', (ord(symbol) for symbol in symbols)))
