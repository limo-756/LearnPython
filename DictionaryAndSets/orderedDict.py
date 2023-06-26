import collections

if __name__ == '__main__':
    ordered_mapping = collections.OrderedDict({'a': 5, 'a': 18, 'b': 34, 'c': 34})
    print(ordered_mapping)
    ordered_mapping['g'] = 12
    ordered_mapping['b'] = 12
    print(ordered_mapping)
    ordered_mapping.move_to_end('a', last=True)
    print(ordered_mapping)
