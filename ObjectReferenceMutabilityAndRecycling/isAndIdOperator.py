if __name__ == '__main__':
    charles = {"name": "Serpent", "occupation": "Thief", "income": 10}
    serpent = charles
    print(serpent)
    print(serpent is charles)
    print(id(serpent), id(charles))

    ajay = {"name": "Serpent", "occupation": "Thief", "income": 10}
    print(ajay == serpent)
    print(ajay is not serpent)
    print(id(ajay), id(serpent))
