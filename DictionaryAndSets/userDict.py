import collections


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    # def __getitem__(self, key):
    #     if str(key) in self.data:
    #         return self.data[str(key)]
    #     else:
    #         raise KeyError(key)
    #
    # def get(self, key, default=None):
    #     try:
    #         return self[key]
    #     except KeyError:
    #         return default

    def __setitem__(self, key, value):
        self.data[str(key)] = value

    def __contains__(self, key):
        return str(key) in self.data


if __name__ == '__main__':
    d = StrKeyDict({2: 'two', 4: 'four'})
    print(d[2])
    print(d[4])
    print(d.get(2))
    print(d.get(4))
    print(d.get(1, 'N/a'))
    print(2 in d)
    print(1 in d)
