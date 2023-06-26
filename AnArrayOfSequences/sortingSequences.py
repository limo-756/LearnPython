fruits = ['grapes', 'raspberry', 'apple', 'banana']

if __name__ == '__main__':
    print("original seq : ", fruits)
    print("default sorting : ", sorted(fruits))
    print("length sorting : ", sorted(fruits, key=len))
    print("reverse length sorting : ", sorted(fruits, key=len, reverse=True))
    print("reverse alphabetical sorting : ", sorted(fruits, key=str, reverse=True))
    print("original sequence : ", fruits)
    fruits.sort()
    print("built-in sort : ", fruits)
