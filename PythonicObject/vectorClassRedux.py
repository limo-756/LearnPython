from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x: 'float', y: 'float') -> None:
        super().__init__()
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self) -> str:
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other: object) -> bool:
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self) -> int:
        return hash(self.x) ^ hash(self.y)

    def __complex__(self):
        return "(%r, !%r)" % self

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec: str) -> str:
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coord = (abs(self), self.angle())
            outer_format_spec = '<{}, {}>'
        else:
            coord = self
            outer_format_spec = '({}, {})'
        components = (format(c, format_spec) for c in coord)
        return outer_format_spec.format(*components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


class ShortVector2d(Vector2d):
    typecode = 'f'


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    print(x, y)
    print(v1)
    print(repr(v1))
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    print(v1)
    octets = bytes(v1)
    print(octets)
    print(Vector2d.frombytes(octets))
    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))
    print(format(v1))
    print(format(v1, '.2f'))
    print(format(v1, '.3e'))
    print(format(v1, '.3fp'))
    print(format(v1, '.3ep'))
    print(format(v1, 'p'))
    print("hash of v1 : ", hash(v1))
    print("hash of v2 : ", hash(Vector2d(3.1, 4.2)))
    print({v1, Vector2d(3.1, 4.2)})

    # Tests of angle
    print(Vector2d(0, 0).angle())
    print(Vector2d(1, 0).angle())
    epsilon = 10 ** -8
    print("epsilon -> ", epsilon)
    print("PI -> ", math.pi)
    print("PI/2 -> ", math.pi / 2)
    print("PI/4 -> ", math.pi / 4)
    print("0,1 angle -> ", Vector2d(0, 1).angle())
    print("1,1 angle -> ", Vector2d(1, 1).angle())
    print(abs(Vector2d(0, 1).angle() - math.pi / 2) < epsilon)
    print(abs(Vector2d(1, 1).angle() - math.pi / 4) < epsilon)

    print(v1.__dict__)

    print(bytes(v1))
    print(len(bytes(v1)))
    v1.typecode = 'f'
    print(bytes(v1))
    print(len(bytes(v1)))
    print(v1.typecode)
    print(Vector2d.typecode)

    sv = ShortVector2d(1/11, 1/27)
    print(bytes(sv))
    print(len(bytes(sv)))
