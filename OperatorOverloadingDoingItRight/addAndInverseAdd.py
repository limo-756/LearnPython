import InterfacesFromProtocolsToABCs.inheritence


class AddableBingoCage(InterfacesFromProtocolsToABCs.inheritence.BingoCage):

    def __add__(self, other):
        if isinstance(other, InterfacesFromProtocolsToABCs.inheritence.Tambola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, InterfacesFromProtocolsToABCs.inheritence.Tambola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self

    def __len__(self):
        return len(self._items)


if __name__ == '__main__':
    vowels = 'AEIOU'
    globe = AddableBingoCage(vowels)
    print(globe.pick() in vowels)
    print(globe.inspect())

    globe2 = AddableBingoCage('XYZ')
    globe3 = globe + globe2
    print(len(globe3))

    # void = globe + [10, 20]
    # TypeError: unsupported; operand; type(s)for +: 'AddableBingoCage' and 'list'

    globe_orig = globe
    print(len(globe.inspect()))
    globe += globe2
    print(globe)

    globe += ['M', 'N']
    print(len(globe.inspect()))

    print(globe is globe_orig)

    # globe += 1
