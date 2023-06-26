import weakref


class Cheese:
    def __init__(self, kind) -> None:
        super().__init__()
        self.kind = kind

    def __repr__(self) -> str:
        return 'Cheese(%r)' % self.kind


if __name__ == '__main__':
    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

    for cheese in catalog:
        stock[cheese.kind] = cheese

    print(sorted(stock.keys()))

    del catalog
    print(sorted(stock.keys()))
    del cheese
    print(sorted(stock.keys()))


    t1 = (1, 2, 3)
    t2 = tuple(t1)
    print(id(t1), id(t2))
    print(t1 is t2)
    t3 = t1[:]
    print(id(t1), id(t3))
    print(t1 is t3)

    s1 = 'ABC'
    s2 = 'ABC'
    print(id(s1), id(s2))
    print(s1 is s2)
