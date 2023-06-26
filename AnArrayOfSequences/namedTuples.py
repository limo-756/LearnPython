from collections import namedtuple

# City = namedtuple('City', 'name countryCode population coord')
City = namedtuple('City', ('name', 'countryCode', 'population', 'coord'))
LatLong = namedtuple('LatLong', 'lat long')

if __name__ == '__main__':
    city = City('Tokyo', 'JP', 36.933, (35.64523, 139.234543))
    print(city)
    print(city.population)
    print(city.countryCode)

    print(City._fields)
    delhi = ('Delhi NCR', 'IN', 21.987, LatLong(19.36827, -99.238762))
    delhi_city = City._make(delhi)
    print(delhi_city)
    print(delhi_city._asdict())

    for key, value in delhi_city._asdict().items():
        print(key, " : ", value)
