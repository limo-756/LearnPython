def dict_construction():
    a = dict([('India', 91), ('America', 1), ('Australia', 32)])
    print(a)
    b = dict((('India', 91), ('America', 1), ('Australia', 32)))
    print(b)
    c = {'India': 91, 'America': 1, 'Australia': 32}
    print(c)
    d = dict(zip(('India', 'America', 'Australia'), (91, 1, 32)))
    print(d)
    e = dict({'India': 91, 'America': 1, 'Australia': 32})
    print(e)
    f = dict(India=91, America=1, Australia=32)
    print(f)

    print(a == b == c == d == e == f)


def dict_comprehension():
    DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan')
    ]

    country_codes = {country: code for code, country in DIAL_CODES}
    print(country_codes)

    country_codes = {country: code for code, country in DIAL_CODES if code < 66}
    print(country_codes)

    country_codes = {code: country.upper() for code, country in DIAL_CODES if code < 66}
    print(country_codes)


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        else:
            return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    dict_construction()
    dict_comprehension()

    d = StrKeyDict0({2: 'two', 4: 'four'})
    print(d[2])
    print(d[4])
    print(d.get(2))
    print(d.get(4))
    print(d.get(1, 'N/a'))
    print(2 in d)
    print(1 in d)
