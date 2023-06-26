import numpy
import array
import random


def basic_operations():
    global a
    a = numpy.arange(12)
    print(a)
    print(type(a))
    print(a.shape)
    a.shape = 3, 4
    print(a.shape)
    print(a)
    print(a[2])
    print(a[2][1])
    print(a[:, 1])
    print(a.transpose())


if __name__ == '__main__':
    basic_operations()
    a = array.array('d', (random.random() for i in range(10 ** 7)))
    fp = open('../output/floats.txt', 'w')
    a.tofile(fp)
    fp.close()

    fp = open('../output/floats.txt', 'r')
    floats = numpy.load(fp)
    print(floats[-3, :])
