import time


def timer(f):
    def i(*args):
        s = time.time()
        r = f(*args)
        print('t: ', time.time() - s)
        print('r:', r)
        return r

    return i
