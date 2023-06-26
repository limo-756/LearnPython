from datetime import datetime

if __name__ == '__main__':
    brl = 1 / 2.43
    print(brl)
    print(format(brl, '0.4f'))
    print(format(42, 'b'))
    print(format(2 / 3, '.1%'))
    print('1 BRL = {rate:0.2f} USD'.format(rate=brl))
    now = datetime.now()
    print(format(now, '%H:%M:%S'))
    print("It's now {:%I:%M %p}".format(now))
