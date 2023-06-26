l = [1, 2, 3]
m = (1, 2, 3)

if __name__ == '__main__':
    print(l)
    print(id(l))
    l += l
    print(l)
    print(id(l))
    print(m)
    print(id(m))
    m *= 3
    print(id(m))
    print(m)
