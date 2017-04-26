def exclusive(a, b):
    it = iter(b)
    y = next(it)
    for x in a:
        found = False
        while x >= y:
            if x == y:
                found = True
                break
            else:
                y = next(it)
        if not found:
            yield x

a = [1, 2, 3, 5, 6, 8, 10, 10, 12, 15, 16, 20, 21, 24, 25, 27]
b = [1, 3, 4, 5, 7, 8, 10, 12, 14, 15, 16, 18, 22, 24, 27]

res = [z for z in exclusive(a, b)]
print res
