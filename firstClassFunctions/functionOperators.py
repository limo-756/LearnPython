from functools import reduce
from operator import mul
from operator import itemgetter
from operator import attrgetter
from collections import namedtuple
from operator import methodcaller
from functools import partial
import unicodedata

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n))


def fact2(n):
    return reduce(mul, range(1, n))


metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.64523, 139.234543)),
    ('Delhi NCR', 'IN', 21.987, (19.36827, -99.238762)),
    ('Mexico City', 'MX', 20.142, (19.43333, -99.13333)),
    ('New York-Newark', 'US', 20.104, (40.80587, -74.876234)),
    ('Sao Palo', 'BR', 19.674, (-23.718, -46.47286))
]


def tag(name, *contents, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, val) for (attr, val) in attrs.items())
    else:
        attr_str = ''
    if contents:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in contents)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    print(fact(10))
    print(fact2(10))

    # itemgetter
    print(sorted(metro_areas, key=itemgetter(1)))

    # attrgetter
    metropolis_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_areas]
    print(metropolis_areas[0])
    print(metropolis_areas[0].coord.lat)
    name_lat = attrgetter('name', 'coord.lat')

    for city in sorted(metropolis_areas, key=attrgetter('coord.lat')):
        print(name_lat(city))

    # methodCaller
    s = 'time for us has come'
    upper = methodcaller('upper')
    hiphenate = methodcaller('replace', ' ', '-')
    print(upper(s))
    print(hiphenate(upper(s)))

    # partial
    triple = partial(mul, 3)
    print(triple(7))

    print(list(map(triple, range(1, 10))))

    str1 = 'café'
    str2 = 'cafe\u0301'
    nfc = partial(unicodedata.normalize, 'NFC')
    print(str1 == str2)
    print(nfc(str1) == nfc(str2))

    # partial with tag
    picture = partial(tag, 'img', cls='pictures')
    print(picture(src='/tmp/pictures'))
    print(picture)
    print(picture.func)
    print(picture.args)
    print(picture.keywords)
