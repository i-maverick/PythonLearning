class Node:
    def __init__(self, val=None, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return self.val


class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, val):
        if (self.root):
            self._add(val, self.root)
        else:
            self.root = Node(val)

    def _add(self, val, currentNode):
        if val < currentNode.val:
            if currentNode.left:
                self._add(val, currentNode.left)
            else:
                currentNode.left = Node(val, currentNode)
        else:
            if currentNode.right:
                self._add(val, currentNode.right)
            else:
                currentNode.right = Node(val, currentNode)


# def flatten(self):
#         self.flat = []
#         self._addFlat(self.root)
#         return self.flat
#     
#     def _addFlat(self, currentNode):
#         self.flat.append(currentNode.val)
#         if currentNode.left:
#             self._addFlat(currentNode.left)
#         if currentNode.right:
#             self._addFlat(currentNode.right)

#     def dublicates(self):
#         self.dublicates = {}
#         self._checkNode(self.root)
#         return self.dublicates
# 
#     def _checkNode(self, currentNode):
#             if currentNode.val in self.dublicates:
#                 self.dublicates[currentNode.val] += 1
#             else:
#                 self.dublicates[currentNode.val] = 1
# 
#             if currentNode.left:
#                 self._checkNode(currentNode.left)
# 
#             if currentNode.right:
#                 self._checkNode(currentNode.right)

#     def __str__(self):
#         return str(self.root.val)

tree = Tree()
tree.addNode(5)
tree.addNode(7)
tree.addNode(3)
tree.addNode(6)
tree.addNode(4)
tree.addNode(5)
tree.addNode(3)
tree.addNode(8)


# flat = tree.flatten()
# print(flat)

def countRepeats(tree):
    if tree.root == None:
        return

    def nextNode(currentNode):
        if currentNode.val in repeats:
            repeats[currentNode.val] += 1
        else:
            repeats[currentNode.val] = 1

        if currentNode.left:
            nextNode(currentNode.left)

        if currentNode.right:
            nextNode(currentNode.right)

    repeats = {}
    nextNode(tree.root)
    return repeats


def mostFrequent(repeats):
    mostFrequent = []
    maxCount = 0
    for key, val in repeats.items():
        if val >= maxCount:
            mostFrequent.append(key)
            maxCount = val
        elif key in mostFrequent:
            mostFrequent.remove(key)
    if maxCount == 1:
        return
    return mostFrequent


repeats = countRepeats(tree)
if repeats == None:
    print("Tree is empy")
else:
    frequent = mostFrequent(repeats)
    if frequent == None:
        print("All elements are unique")
    else:
        print(frequent)
