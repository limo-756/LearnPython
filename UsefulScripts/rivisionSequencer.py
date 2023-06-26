import random

if __name__ == '__main__':
    n = 17
    chapters = [i + 1 for i in range(n)]
    print(chapters)
    print("The revision seq is ->")
    random.shuffle(chapters)
    print(chapters)
