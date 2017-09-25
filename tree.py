class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.items = [0]

    def height(self, idx=1):
        if idx < len(self.items):
            lh = self.height(idx * 2)
            rh = self.height(idx * 2 + 1)
            return max(lh, rh) + 1
        else:
            return 0


tree = Tree()
tree.items.extend([5, 9, 11, 14, 18, 19, 21, 33, 17, 27, 7])

print(tree.height())


def max_height(node):
    if node:
        return max(max_height(node.left), max_height(node.right)) + 1
    else:
        return 0


def min_height(node):
    if node:
        return min(min_height(node.left), min_height(node.right)) + 1
    else:
        return 0


def is_balanced(node):
    return max_height(node) - min_height(node) <= 1


def add_to_tree(arr, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    node = Node(mid)
    node.left = add_to_tree(arr, start, mid - 1)
    node.right = add_to_tree(arr, mid + 1, end)
    return node


def create_min_bst(arr):
    return add_to_tree(arr, 0, len(arr) - 1)
