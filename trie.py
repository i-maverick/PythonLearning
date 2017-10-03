class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = dict()
        self.last = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        node = self.root
        for letter in word:
            if letter not in node.next:
                node.next[letter] = Node(letter)
            node = node.next[letter]
        node.last = True

    def print(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.next:
                print(node.next.keys())
                queue.extend(node.next.values())

    def size(self):
        n = 0
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.last:
                n +=1
            if node.next:
                queue.extend(node.next.values())
        return n

    def find(self, word):
        node = self.root
        for letter in word:
            if letter not in node.next:
                return False
            node = node.next[letter]
        return node.last


def max_height(node):
    if node and node.next:
        return max(max_height(n) for n in node.next.values()) + 1
    else:
        return 0


def min_height(node):
    if node and node.next:
        return min(min_height(n) for n in node.next.values()) + 1
    else:
        return 0


trie = Trie()
trie.add_word('one')
trie.add_word('man')
trie.add_word('mansion')
trie.add_word('mini')
trie.add_word('poni')
trie.add_word('pons')

trie.print()
print(trie.size())
print(max_height(trie.root))
print(min_height(trie.root))

print(trie.find('on'))
print(trie.find('one'))
print(trie.find('man'))
print(trie.find('mans'))
print(trie.find('min'))
print(trie.find('mini'))
