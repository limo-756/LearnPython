import decimal
from collections import Counter

if __name__ == '__main__':
    ctx = decimal.getcontext()
    ctx.prec = 40
    one_third = decimal.Decimal('1') / decimal.Decimal('3')
    print(one_third)
    print(one_third == +one_third)
    ctx.prec = 28
    print(one_third == +one_third)
    print(+one_third)

    ct = Counter('abrakadabra')
    print(ct)
    ct['r'] = -3
    ct['d'] = 0
    print(ct)
    print(+ct)
