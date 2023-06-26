class Vec:
    __slots__ = ('x', 'y')

    def __init__(self, x, y) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = x + y


if __name__ == '__main__':
    v = Vec(1, 2)
    print(v.x)
    print(v.y)
    print(v.z)
