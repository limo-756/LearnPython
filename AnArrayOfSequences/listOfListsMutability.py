board1 = [['_'] * 3] * 3
board2 = [['_'] * 3 for i in range(3)]

if __name__ == '__main__':
    print(board1)
    board1[1][1] = 'X'
    print(board1)
    print("Now printing board2")
    print(board2)
    board2[1][1] = 'X'
    print(board2)
