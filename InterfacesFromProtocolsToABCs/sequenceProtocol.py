class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


if __name__ == '__main__':
    f = Foo()
    print(f[1])
    print([i for i in f])
    print(20 in f)
    print(25 in f)
