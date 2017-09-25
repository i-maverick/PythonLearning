from itertools import zip


def is_palindrom(s):
    t = [x.lower() for x in s if x.isalnum()]  # additional string of len(t)
    for x, y in zip(t, reversed(t)):
        if x != y:
            return False
    return True


def is_palindrom1(s):
    it = iter(s)
    it_rev = reversed(s)
    for x,y in zip(it, it_rev):  # with itertools
        while not x.isalnum():
            x = next(it)
        while not y.isalnum():
            y = next(it_rev)
        if str.lower(x) != str.lower(y):
            return False
    return True


s = 'A roza upala na lapu Azora!'
print(is_palindrom(s))
print(is_palindrom1(s))
