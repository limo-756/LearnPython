colors = ['white', 'black']
sizes = ['s', 'm', 'l']


def generator_function_to_avoid_new_list_creation():
    for shirt in ('%s, %s' % (color, size) for color in colors for size in sizes):
        print(shirt)


if __name__ == '__main__':
    shirts = [[color, size] for color in colors for size in sizes]
    print(shirts)
    generator_function_to_avoid_new_list_creation()
