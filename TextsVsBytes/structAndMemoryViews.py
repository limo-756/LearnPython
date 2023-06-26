import struct

fmt = '<3s3sHH'
if __name__ == '__main__':
    with open('/Users/anurag.sh/workspace/SQLDump/memView.gif', 'rb') as fp:
        img = memoryview(fp.read())

    header = img[:10]
    print(header)
    print(bytes(header))
    print(struct.unpack(fmt, header))
    del header
    del img
