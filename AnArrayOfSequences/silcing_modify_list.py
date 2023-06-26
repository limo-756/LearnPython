number_list = list(range(10))

if __name__ == '__main__':
    print(number_list)
    number_list[2:5] = [20, 30]
    print(number_list)
    del number_list[5:7]
    print(number_list)
    number_list[3::2] = [11, 22]
    print(number_list)
