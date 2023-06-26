import array

if __name__ == '__main__':
    a = array.array('h', (-2, -1, 0, 1, 2))
    print(a)
    memv = memoryview(a)
    print(len(memv))
    print(memv[0])
    memv_oct = memv.cast('B')
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(a)