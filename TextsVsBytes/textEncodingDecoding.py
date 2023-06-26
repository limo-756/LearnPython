import os

filename = '../output/cafe.txt'

if __name__ == '__main__':
    print("Writing the file")
    fp = open(filename, 'w', encoding='utf_8')
    print(fp)
    fp.write('Café')
    fp.close()
    print('File size : ', os.stat(filename).st_size)

    print("Reading the file with default encoding")
    fp2 = open(filename)
    print(fp2)
    print(fp2.encoding)
    print(fp2.read())

    print("reading file with utf_8 encoding")
    fp3 = open(filename, encoding='utf_8')
    print(fp3)
    print(fp3.encoding)
    print(fp3.read())

    print("reading file in rb mode")
    fp4 = open(filename, 'rb')
    print(fp4)
    print(fp4.read())