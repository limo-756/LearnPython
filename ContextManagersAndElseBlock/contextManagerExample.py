import sys
import contextlib


@contextlib.contextmanager
def looking_glass():
    original_writer = sys.stdout.write

    def reverse_write(text):
        original_writer(text[::-1])

    sys.stdout.write = reverse_write

    try:
        msg = ''
        yield "AAAZZZ"
    except ZeroDivisionError:
        msg = 'You are not allowed to devide by zero'
    finally:
        sys.stdout.write = original_writer
        if msg:
            print(msg)


if __name__ == '__main__':
    with(looking_glass()) as looking:
        print("Abra ka dabra")
        print(looking)
        print(1/0)

    print(looking)
    print("Should print normal")
