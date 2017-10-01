class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.items = []

tree = Tree()
tree.items = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27, 7]


def height(idx=0):
    if idx < len(tree.items):
        lh = height(idx * 2 + 1)
        rh = height(idx * 2 + 2)
        return max(lh, rh) + 1
    else:
        return 0


print(height())


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


def isBST(node):
    return (isBSTUtil(node, float("-inf"), float("inf")))


def isBSTUtil(node, mini, maxi):
    if node is None:
        return True
    if node.data < mini or node.data > maxi:
        return False
    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))


from collections import defaultdict
level_values = defaultdict(int)

def go_depth(node, level=1):
    if not node:
        return
    level_values[level] += node.data
    go_depth(node.left, level + 1)
    go_depth(node.right, level + 1)
