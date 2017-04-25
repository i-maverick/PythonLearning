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

print 'mid: {}'.format(m)
