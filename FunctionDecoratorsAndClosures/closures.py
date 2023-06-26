def averagers():
    avg = []

    def calculate_averagers(num):
        avg.append(num)
        return sum(avg) / len(avg)

    return calculate_averagers


if __name__ == '__main__':
    avg = averagers()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__[0])
    print(avg.__closure__[0].cell_contents)
