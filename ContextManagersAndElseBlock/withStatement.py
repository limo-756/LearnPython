import sys


class LookingGlass:

    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JJJAAASSSSDDDD'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, traceback):
        sys.stdout.write = self.original_write
        if exc_val is ZeroDivisionError:
            print('PLease Do not divide by zero!')
            return True


def looking_glass_context_manager():
    with(LookingGlass()) as looking:
        print("Abra ka dabra")
        print(looking)

    print(looking)
    print("Should print normal")

    manager = LookingGlass()
    print(manager)
    monster = manager.__enter__()
    print(monster == 'JJJAAASSSSDDDD')
    print(monster)
    print(manager)
    manager.__exit__(None, None, None)
    print(monster)
    print(manager)


if __name__ == '__main__':
    with open('/Users/anurag.sh/PycharmProjects/LearnPython/ContextManagersAndElseBlock/withStatement.py') as fp:
        src = fp.read()

    print(len(src))
    print(src)
    print(fp)
    print(fp.closed, fp.encoding)

    looking_glass_context_manager()
