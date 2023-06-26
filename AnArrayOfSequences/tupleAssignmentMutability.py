t = (1, 2, [3, 4])

if __name__ == '__main__':
    print("This is initial", t)
    a = None
    
    try:
        # t[2] += [5, 6]
        a = t[2]
        a = a + [5, 6]
    except BaseException:
        print(BaseException)

    print(t)
    print(a)
