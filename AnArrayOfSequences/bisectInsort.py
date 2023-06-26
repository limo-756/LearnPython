import bisect
import random

SIZE = 10
my_list = []

if __name__ == '__main__':
    for i in range(SIZE):
        num = random.randrange(SIZE * 2)
        bisect.insort(my_list, num)
        print(num, " -> ", my_list)

    print(my_list)