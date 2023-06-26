from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        return Vector(self.x * scale, self.y * scale)

    def __truediv__(self, scale):
        return Vector(self.x / scale, self.y / scale)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
    print(v1 - v2)
    v = Vector(3, 4)
    print(v * 3)
    print(v / 3)
    print(abs(v))
    print(abs(v * 3))
    print(bool(v))
