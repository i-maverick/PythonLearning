import functools
import sys
import time


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('started', func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner


def trace_with_handle(func=None, *, handle=sys.stdout):
    if func is None:
        return lambda func: trace_with_handle(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('started', func.__name__, args, kwargs, file=handle)
        return func(*args, **kwargs)
    return inner


@trace
def do_nothing(i):
    print('do nothing {}'.format(i))

do_nothing(1)


def timethis(func=None, *, n_iter=10):
    if func is None:
        return lambda func: timethis(func, n_iter=n_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('started', func.__name__, args, kwargs)
        acc = float('inf')
        for i in range(n_iter):
            tick = time.perf_counter()
            result = func(*args, **kwargs)
            acc = min(acc, time.perf_counter() - tick)
        print(acc)
        return result
    return inner


@timethis(n_iter=1000)
def summa():
    s = sum(range(1000000))

summa()
