from array import array
import math
import reprlib
import numbers
import functools
import operator
import itertools


class Vector:
    typecode = 'd'

    def __init__(self, components) -> None:
        super().__init__()
        self.__components = array(self.typecode, components)

    @property
    def components(self):
        return self.__components

    # @property
    # def x(self):
    #     return self.components[0]
    #
    # @property
    # def y(self):
    #     return self.components[1]
    #
    # @property
    # def z(self):
    #     return self.components[2]

    def __iter__(self):
        return iter(self.components)

    def __repr__(self) -> str:
        components = reprlib.repr(self.components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self) -> str:
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])) + bytes(self.components)

    def __eq__(self, other: object) -> bool:
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self.components[index])
        elif isinstance(index, numbers.Integral):
            return self.components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self.components):
                return self.components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif key.islower():
                error = "can't set attributes 'a' to 'z' in {attr_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=key)
                raise AttributeError(msg)
        super().__setattr__(key, value)

    def __hash__(self):
        return functools.reduce(operator.xor, map(hash, self.components), 0)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, format_spec):
        if format_spec.endswith('h'):
            format_spec = format_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'

        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


def vector_2d_test():
    v1 = Vector([3, 4])
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
    print(Vector.frombytes(octets))
    print(abs(v1))
    print(bool(v1), bool(Vector([0, 0])))
    print(format(v1))
    print(format(v1, '.2f'))
    print(format(v1, '.3e'))
    print(format(v1, '.3fh'))
    print(format(v1, '.3eh'))
    print(format(v1, 'h'))
    print("hash of v1 : ", hash(v1))
    print("hash of v2 : ", hash(Vector([3.1, 4.2])))
    print({v1, Vector([3.1, 4.2])})

    # Tests of angle
    print(Vector([0, 0]).angles())
    print(Vector([1, 0]).angles())
    epsilon = 10 ** -8
    print("epsilon -> ", epsilon)
    print("PI -> ", math.pi)
    print("PI/2 -> ", math.pi / 2)
    print("PI/4 -> ", math.pi / 4)
    print("0,1 angle -> ", Vector([0, 1]).angles())
    print("1,1 angle -> ", Vector([1, 1]).angles())

    print(v1.__dict__)

    print(bytes(v1))
    print(len(bytes(v1)))
    v1.typecode = 'f'
    print(bytes(v1))
    print(len(bytes(v1)))
    print(v1.typecode)
    print(Vector.typecode)


if __name__ == '__main__':
    print(Vector([3.1, 4.2]))
    print(Vector((3, 4, 5)))
    print(Vector(range(10)))
    v1 = Vector([3, 4, 5])
    print(len(v1))
    print(v1[0], v1[-1])
    v7 = Vector(range(7))
    print(v7[1:4])
    print(v7[-1])
    print(v7[-1:])
    # print(v7[1, 2])

    print("###############")
    print(v7.x, v7.y, v7.z)
    # v7.x = 1000
    print(hash(v7))

    ## formating test
    v3 = Vector([3, 4, 5])
    print(format(v3))
    print(format(Vector(range(7))))

    print("Formatting -------------")
    print(format(Vector([1, 1]), 'h'))
    print(format(Vector([1, 1]), '.3eh'))
    print(format(Vector([1, 1]), '.5fh'))
    print(format(Vector([1, 1, 1]), 'h'))
    print(format(Vector([2, 2, 2]), '.3eh'))
    print(format(Vector([0, 0, 0]), '.5fh'))
    print(format(Vector([-1, -1, -1, -1]), 'h'))
    print(format(Vector([2, 2, 2, 2]), '.3eh'))
    print(format(Vector([0, 1, 0, 0]), '.5fh'))

    print("Vector2d backward compatibility ------->")
    vector_2d_test()
