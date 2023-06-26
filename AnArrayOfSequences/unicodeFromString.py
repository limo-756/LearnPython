symbols = "$€£¥₹₿"


def simple_way():
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)


def generator_function_way():
    codes = [ord(symbol) for symbol in symbols]
    print(codes)


def generator_function_way_for_non_ascii_symbols():
    codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
    print(codes)


def filter_map_way_for_non_ascii_symbols():
    codes = list(filter(lambda s: s > 127, map(ord, symbols)))
    print(codes)


if __name__ == '__main__':
    simple_way()
    generator_function_way()
    generator_function_way_for_non_ascii_symbols()
    filter_map_way_for_non_ascii_symbols()
