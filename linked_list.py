# 6 -> 3 -> 2 -> 5 -> 4 -> 7


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head
        while node and node.data:
            print(node.data)
            node = node.next

lst = LinkedList()
n6 = Node(6)
n3 = Node(3)
n2 = Node(2)
n5 = Node(5)
n4 = Node(4)
n7 = Node(7)

lst.head = n6
n6.next = n3
n3.next = n2
n2.next = n5
n5.next = n4
n4.next = n7


def remove_node(node):
    next = node.next
    node.data = next.data
    node.next = next.next


lst.print()
remove_node(n5)
print("")
lst.print()
