class Demo:
    @classmethod
    def classmethod(*args):
        return args

    @staticmethod
    def staticmethod(*args):
        return args


if __name__ == '__main__':
   print(Demo.classmethod())
   print(Demo.classmethod("spam"))
   print(Demo.staticmethod())
   print(Demo.staticmethod("spam"))