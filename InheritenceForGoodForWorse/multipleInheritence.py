import numbers


class A:

    def ping(self):
        print("ping:", self)


class B:

    def pong(self):
        print("pong:", self)


class C:

    def pong(self):
        print("PONG:", self)


class D(B, C):

    def ping(self):
        super().ping()
        print("post-ping", self)

    def pingpong(self):
        self.ping()
        super.ping()
        self.pong()
        super.pong()
        C.pong(self)


def print_mro(cls):
    print(",".join(c.__name__ for c in cls.__mro__))


if __name__ == '__main__':
    d = D()
    d.pong()
    C.pong(d)
    print_mro(bool)
    print_mro(D)
    print_mro(numbers.Integral)
