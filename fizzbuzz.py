from sqlite3 import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node

        self.tail = node

    def removeNode(self, data):
        prev = None
        node = self.head
        while node and node.data != data:
            prev = node
            node = node.next

        if prev:
            prev.next = node.next
        else:
            self.head = node.next

    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


lst = LinkedList()
lst.addNode(2)
lst.addNode(0)
lst.addNode(6)
lst.addNode(3)
lst.addNode(5)
lst.addNode(1)

lst.printList()

a = lst.head
m = lst.head
l = 0
while a:
    l += 1
    if l % 2 == 0:
        m = m.next
    a = a.next

print("mid:", m)


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
