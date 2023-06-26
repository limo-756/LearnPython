from unicodedata import normalize, name

if __name__ == '__main__':
    s1 = 'Café'
    s2 = 'Cafe\u0301'
    print(len(s1), len(s2))

    print("NFC Composition")
    print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
    print((normalize('NFC', s1)), (normalize('NFC', s2)))
    print((normalize('NFC', s1)) == (normalize('NFC', s2)))

    print("NFD decomposition")
    print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
    print((normalize('NFD', s1)), (normalize('NFD', s2)))
    print((normalize('NFD', s1)) == (normalize('NFD', s2)))

    print("Omega char normalization")
    ohm = '\u2126'
    print(ohm)
    print(name(ohm))
    ohm_c = normalize('NFC', ohm)
    print(ohm_c)
    print(name(ohm_c))
    print(ohm == ohm_c)
    print(normalize('NFC', ohm) == ohm_c)
    print(normalize('NFC', ohm) == normalize('NFC', ohm_c))

    half = '½'
    micro = 'μ'

    print("half sign compatibility normalization")
    print(half)
    print(name(half))
    print(normalize('NFKC', half))

    print("micro sign compatibility normalization")
    print(micro)
    print(name(micro))
    print(normalize('NFKC', micro))
