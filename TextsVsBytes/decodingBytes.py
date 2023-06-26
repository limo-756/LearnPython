if __name__ == '__main__':
    octets = b'Montr\xe9al'
    print(octets.decode('cp1252'))
    print(octets.decode('iso8859_7'))
    print(octets.decode('koi8_r'))
    print(octets.decode('utf_8', errors='replace'))
    print(octets.decode('utf_8'))
