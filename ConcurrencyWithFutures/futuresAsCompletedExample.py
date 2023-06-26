import os, time, sys
import requests
from concurrent import futures

G20_CC = 'CN IN US ID BR NG BD RU JP MX PH VN ET EG DE IR TR CD FR UK'.split()

BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = '/Users/anurag.sh/workspace/SQLDump/temp/'


def save_flags(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with(open(path, 'wb')) as fp:
        fp.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flags(image, cc.lower() + '.gif')

    return len(cc_list)


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flags(image, cc.lower() + '.gif')
    return cc


MAX_WORKERS = 20


def concurrent_many(cc_list):
    with(futures.ThreadPoolExecutor(max_workers=3)) as threadPool:
        to_do = []
        for cc in sorted(cc_list):
            future = threadPool.submit(download_one, cc)
            to_do.append(future)
            msg = 'attached {} with {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


def main(strategy):
    t0 = time.time()
    count = strategy(G20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    # main(download_many)
    main(concurrent_many)
