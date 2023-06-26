def duck_typing(field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)
    print(field_names)


if __name__ == '__main__':
    duck_typing('this,is,a,statement')
    duck_typing(['this', 'is', 'India'])
