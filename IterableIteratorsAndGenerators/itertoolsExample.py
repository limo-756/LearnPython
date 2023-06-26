import itertools
import operator


def vowel(c):
    return c.lower() in 'aeiou'


if __name__ == '__main__':
    gen = itertools.count(1, .5)
    for i in range(3):
        print(next(gen))

    gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
    print(list(gen))

    name = 'Aardvark'

    # produce sub-set of items, without change state od item
    print(list(filter(vowel, name)))
    print(list(itertools.filterfalse(vowel, name)))
    print(list(itertools.dropwhile(vowel, name)))
    print(list(itertools.takewhile(vowel, name)))
    print(list(itertools.compress(name, (1, 0, 1, 1, 0, 1))))
    print(list(itertools.islice(name, 4)))
    print(list(itertools.islice(name, 4, 7)))
    print(list(itertools.islice(name, 1, 7, 2)))

    # map the input item to some new item, without changing the size of the stream
    sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

    # accumulate applies operation to first pair then operation on result next item ...
    print(list(itertools.accumulate(sample)))
    print(list(itertools.accumulate(sample, min)))
    print(list(itertools.accumulate(sample, max)))
    print(list(itertools.accumulate(sample, operator.mul)))
    print(list(itertools.accumulate(range(1, 11), operator.mul)))

    # enumerate produce indexed items, index can be given
    print(list(enumerate('albatroz', 1)))

    # map multiple streams to a function
    print(list(map(operator.mul, range(11), range(11))))
    print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))

    # map stream to function *args
    print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))
    print(list(itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(sample), 1))))

    # chain -> it chains all the streams into single stream
    print(list(itertools.chain('ABC', range(2))))
    print(list(itertools.chain(enumerate('ABC'))))

    # chain.from_iterable -> it works as unpacking of tuple
    print(list(itertools.chain.from_iterable(enumerate('ABC'))))

    # zip -> pack multiple streams into tuples, till the length of smallest stream
    print(list(zip('ABC', range(5))))
    print(list(zip('ABC', range(5), [10, 20, 30, 40])))

    # zip_longest -> pack multiple streams into tuples, till the length of largest stream.
    # we can give fillvalue for custom padding
    print(list(itertools.zip_longest('ABC', range(5))))
    print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))

    # product -> it generates cartesian product of all the stream elements
    print(list(itertools.product('ABC', range(2))))
    print(list(itertools.product('AK', 'spades hearts diamonds clubs'.split())))
    print(list(itertools.product('ABC')))
    print(list(itertools.product('ABC', repeat=2)))
    print(list(itertools.product('ABC', repeat=3)))
    print(list(itertools.product('ABC', range(2), repeat=2)))

    # count -> it generates infinite stream of numbers from start value
    ct = itertools.count(100, .4)
    print(next(ct), next(ct), next(ct))
    print(list(itertools.islice(itertools.count(1, .3), 3)))

    # cycle -> it can iterate over the collection in cycles
    print(list(itertools.islice(itertools.cycle('ANBDCGHJK'), 100, 107)))

    # repeat -> it will repeat the sequence, the optional argument times limit the repeat
    print(list(itertools.islice(itertools.repeat('ABCD'), 3)))
    print(list(itertools.islice(itertools.repeat('ABCD', 2), 3)))
    print(list(map(operator.mul, range(11), itertools.repeat(5))))

    # combinations -> it produces all the combinations of items present in the collection without replacement
    print(list(itertools.combinations('ABC', 2)))

    # combinations_with_replacement -> it produces all the combinations of items
    # present in the collection with replacement
    print(list(itertools.combinations_with_replacement('ABC', 2)))

    # permutations -> it produces all the permutations of the items present in the collection
    print(list(itertools.permutations('ABC', 2)))

    # groupby -> group all the items in the collections,
    # you can access the item and list of all items that are same
    print(list(itertools.groupby('LALAELAELEA')))
    for char, group in itertools.groupby('LLLLLAAAAEEEEEPP'):
        print(char, ' -> ', list(group))

    animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphine', 'shark', 'lion']
    animals.sort(key=len)
    print(animals)

    for length, group in itertools.groupby(animals, len):
        print(length, ' -> ', list(group))

    # reversed -> reverses the sequence
    for length, group in itertools.groupby(reversed(animals), len):
        print(length, ' -> ', list(group))

    # tee ->
    print(list(itertools.tee('ABC')))
    g1, g2 = itertools.tee('ABC')
    print(next(g1), next(g2), next(g2), next(g1), next(g1), next(g2))
    print(list(zip(*itertools.tee('ABC'))))

    # all -> return true if all the items are true
    print(all([1, 2, 3]))
    print(all([1, 0, 3]))
    print(all([]))

    # any -> returns true if any of the item is true
    print(any([1, 2, 3]))
    print(any([1, 0, 3]))
    print(any([0.0, 0]))
    print(any([]))
    g = (n for n in [0., 0., 7, 8])
    print(any(g))
    print(next(g))

