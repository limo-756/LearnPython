def with_yield_from():
    yield from 'AB'
    yield from range(1, 3)


def without_yield_from():
    for i in 'AB':
        yield i

    for i in range(1, 3):
        yield i


# Chaining iterables with yield from
def chain(*iterables):
    for it in iterables:
        yield from it


if __name__ == '__main__':
    print(list(with_yield_from()))
    print(list(without_yield_from()))

    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))
