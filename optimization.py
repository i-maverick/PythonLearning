lst = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]

def f1(list):
    string = ""
    for item in list:
        string = string + chr(item)
    return string

def f2(list):
    return reduce(lambda string, item: string + chr(item), list, "")

def f3(list):
    string = ""
    for character in map(chr, list):
        string = string + character
    return string

def f4(list):
    string = ''
    lchr = chr
    for item in list:
        string = string + lchr(item)
    return string

import string
def f5(list):
    return string.joinfields(map(chr, list), '')

def f6(list):
    return string.join(map(chr, list), '')

import array
def f7(list):
    return array.array('b', list).tostring()

import time
def timing(f, n, a):
    print f.__name__,
    r = range(n)
    t1 = time.clock()
    for i in r:
        f(a)
    t2 = time.clock()
    print round(t2 - t1, 3)

timing(f1, 1000000, lst)
timing(f2, 1000000, lst)
timing(f3, 1000000, lst)
timing(f4, 1000000, lst)
timing(f5, 1000000, lst)
timing(f6, 1000000, lst)
timing(f7, 1000000, lst)
