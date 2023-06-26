import array
import random

if __name__ == '__main__':
    my_array = array.array('d', (random.random() for i in range(10 ** 7)))
    print(my_array[-1])
    fp = open('../output/floats.bin', 'wb')
    my_array.tofile(fp)
    fp.close()
    floats2 = array.array('d')
    fp = open('../output/floats.bin', 'rb')
    floats2.fromfile(fp, 10 ** 7)
    fp.close()
    print(floats2[-1])
    print(floats2 == my_array)
