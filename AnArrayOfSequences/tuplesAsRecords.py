lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32405, 0.66, 8014)
travelers_ids = [('USA', '3195434'), ('BRA', 'C324D9764'), ('ESP', 'P8763FE987')]

if __name__ == '__main__':
    print(lax_coordinates)
    print(city, year, pop, chg, area)
    for passport in sorted(travelers_ids):
        print('%s/%s' % passport)

    for country, _ in travelers_ids:
        print(country)
