import time


def log(func):
    def wrapper(n):
        print "{} {} is started".format(time.strftime('%X'), func.__name__)
        func(n)
        print "{} {} is finished".format(time.strftime('%X'), func.__name__)

    return wrapper


@log
def fib(n):
    a, b = 0, 1
    for _ in xrange(n + 1):
        print a
        a, b = b, a + b


fib(10)
