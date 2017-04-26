import itertools


def is_palindrom(s):
    t = [x.lower() for x in s if x.isalnum()]  # additional string of len(t)
    rev = reversed(t)
    for x, y in itertools.izip(t, rev):
        if x != y:
            return False
    return True


def is_palindrom1(s):
    it = iter(s)
    it_rev = reversed(s)
    for x,y in itertools.izip(it, it_rev):
        while not str.isalnum(x):
            x = next(it)
        while not str.isalnum(y):
            y = next(it_rev)
        if str.lower(x) != str.lower(y):
            return False
    return True


s = 'A roza upala na lapu Azora!'
print is_palindrom(s)
print is_palindrom1(s)
