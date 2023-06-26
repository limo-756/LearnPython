class MySeq:
    def __getitem__(self, item):
        return item


if __name__ == '__main__':
    m = MySeq()
    print(m[1])
    print(m[1:5])
    print(m[1:5:-1])
    print(m[1:5:-1, 3])
    print(m[1:5:-1, 3:11])
    print(m[1:5:-1, 3:11:-3])
    print(m[1:5:-1, 3:11:-3, 13])
    print(m[1:5:-1, 3:11:-3, 13:17])
    print(m[1:5:-1, 3:11:-3, 13:17:-5])
    print(m[1:])
    print(m[:])
    print(m[:, ::-1])
    print(slice)
    print(dir(slice))
    print(slice(None, None, None).indices(10))
    print(slice(-1, None, None).indices(20))
    print(slice(None, 10, 2).indices(5))
    print(slice(-3, None, None).indices(5))
