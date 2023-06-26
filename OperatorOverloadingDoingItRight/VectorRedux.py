from array import array
import math
import reprlib
import numbers
import functools
import operator
import itertools
from fractions import Fraction


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
        if isinstance(other, Vector):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented

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

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            return Vector(x + y for (x, y) in itertools.zip_longest(self, other, fillvalue=0))
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other):
        try:
            return Vector(x * y for (x, y) in itertools.zip_longest(self, other))
        except:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v = Vector([1, 2, 3, 4, 5])
    print(-v)
    print(+v)

    v1 = Vector([3, 4, 5])
    v2 = Vector([6, 7, 8])
    print(v1 + v2)
    print(v1 + v2 == Vector([3 + 6, 4 + 7, 5 + 8]))
    print(Vector([3, 4, 5, 6]) + Vector([1, 2]))

    v1 = Vector([3, 4, 5])
    print(v1 + (10, 20, 30))

    print((10, 20, 30) + v1)
    # TypeError: can only concatenate tuple (not "Vector") to tuple

    # print(v1 + 1)
    # TypeError: 'int' object is not iterable

    # print(v1 + 'abc')
    # TypeError: unsupported; operand; type(s)for +: 'float' and 'str'

    print(v1 * 10)
    print(v1 * True)
    print(v1 * Fraction(1, 3))

    print(Vector([1, 2, 3]) @ Vector([4, 5, 6]))

    print(Vector([1, 2, 3]) == Vector([1, 2, 3]))
    print(Vector([1, 2, 3]) == [1, 2, 3])


