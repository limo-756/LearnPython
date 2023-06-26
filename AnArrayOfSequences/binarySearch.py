import bisect

def example2_grades(score, ranges = [60, 70, 80, 90], grades = 'FDCBA'):
    index = bisect.bisect(ranges, score)
    return grades[index]

haystack = [1, 3, 5, 8, 12, 15, 19, 19, 19, 19, 22, 26, 28, 30, 33, 34, 37, 40, 45, 50]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
row_fmt = '{0:2d} @ {1:2d}    {2}{0:<2d}'

if __name__ == '__main__':

    print(haystack)
    print(bisect.bisect_left(haystack, 25), haystack[bisect.bisect_left(haystack, 25)])
    print(bisect.bisect_right(haystack, 25), haystack[bisect.bisect_right(haystack, 25)])

    print(bisect.bisect_left(haystack, 19), haystack[bisect.bisect_left(haystack, 19)])
    print(bisect.bisect_right(haystack, 19), haystack[bisect.bisect_right(haystack, 19)])

    print(bisect.bisect_left(haystack, 30), haystack[bisect.bisect_left(haystack, 30)])
    print(bisect.bisect_left(haystack, 29), haystack[bisect.bisect_left(haystack, 29)])
    print(bisect.bisect_left(haystack, 31), haystack[bisect.bisect_left(haystack, 31)])

    print(bisect.bisect_right(haystack, 30), haystack[bisect.bisect_right(haystack, 30)])
    print(bisect.bisect_right(haystack, 29), haystack[bisect.bisect_right(haystack, 29)])
    print(bisect.bisect_right(haystack, 31), haystack[bisect.bisect_right(haystack, 31)])

    print('haystack ->', ' '.join('%2d' % n for n in haystack))
    needles.sort(reverse=True)

    for needle in needles:
        pos = bisect.bisect_right(haystack, needle)
        offset = pos * '  |'
        print(row_fmt.format(needle, pos, offset))

    for score in (33, 99, 77, 70, 89, 90, 100):
        print(score, " : ", example2_grades(score))