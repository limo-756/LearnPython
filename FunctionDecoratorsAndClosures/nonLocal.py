def make_averager():
    cnt = 0
    total = 0

    def avg(item):
        cnt += 1
        total += item
        return total / cnt

    return avg


def new_make_averager():
    cnt = 0
    total = 0

    def avg(item):
        nonlocal cnt, total
        cnt += 1
        total += item
        return total / cnt

    return avg


if __name__ == '__main__':
    old_avg = make_averager()
    # print(old_avg(10))

    new_avg = new_make_averager()
    print(new_avg(10))
    print(new_avg(11))
    print(new_avg(12))
