lax_coordinates = (33.9425, -118.408056)
lat, long = lax_coordinates

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.64523, 139.234543)),
    ('Delhi NCR', 'IN', 21.987, (19.36827, -99.238762)),
    ('Mexico City', 'MX', 20.142, (19.43333, -99.13333)),
    ('New York-Newark', 'US', 20.104, (40.80587, -74.876234)),
    ('Sao Palo', 'BR', 19.674, (-23.718, -46.47286))
]

if __name__ == '__main__':
    print(lat)
    print(long)
    long, lat = lat, long
    print(lat)
    print(long)

    print(divmod(20, 8))
    t = (20, 8)
    print(divmod(*t))
    quotient, reminder = divmod(*t)
    print(quotient)
    print(reminder)

    a, b, *rest = range(5)
    print(a, b, rest)
    a, b, *rest = range(4)
    print(a, b, rest)
    a, b, *rest = range(2)
    print(a, b, rest)

    *rest, a, b = range(5)
    print(rest, a, b)
    *rest, a, b = range(2)
    print(rest, a, b)
    a, *rest, b = range(10)
    print(a, rest, b)

    for city, *rest, (longitude, latitude) in metro_areas:
        print('%r, (%r, %r)' % (city, longitude, latitude))

