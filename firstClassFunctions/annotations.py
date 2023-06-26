from inspect import signature


def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """Returned text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


if __name__ == '__main__':
    print(clip('abcd'))
    print(clip('abcd asdaqw'))
    print(clip('abcd asdaqw ewfewdwedwe'))
    print(clip.__annotations__)

    sig = signature(clip)
    print(sig.return_annotation)

    for param in sig.parameters.values():
        print(repr(param.annotation).ljust(13), " : ", param.name.ljust(10), " = ", param.default)
