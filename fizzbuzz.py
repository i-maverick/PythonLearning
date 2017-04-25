import collections


def reverse(s):
    res = []
    for i in range(len(s)):
        res.append(s[len(s) - i - 1])
    return ''.join(res)


s = "askdfgshjkl"
print(reverse(s))

d = {}
for c in s:
    if c in d.keys():
        d[c] += 1
    else:
        d[c] = 1
print([x for x, y in d.items() if y > 1])
print([x for x, y in collections.Counter(s).items() if y > 1])


def fib(n):
    if n == 0:
        yield None
    a, b = 0, 1
    yield a
    for _ in range(n - 1):
        yield b
        a, b = b, b + a


print([x for x in fib(10)])

palindrom = "abba"
print(palindrom == palindrom[::-1])

matrix = [[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
xx = 55


def findMatrix(matrix, xx):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col > 0:
        if matrix[row][col] == xx:
            return row, col
        if matrix[row][col] > xx:
            col -= 1
        else:
            row += 1


print(findMatrix(matrix, xx))
