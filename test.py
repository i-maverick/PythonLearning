from collections import Counter
import time


def dictWord(word):
    d = {}
    for i in word:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def isAnagram(first, second):
    return Counter(first) == Counter(second)


groupAnagrams = ['сон', 'нос', 'сорт', 'трос', 'торт', 'рост']


# [
# ['сон', 'нос'],
# ['сорт', 'трос', 'рост'],
# ['торт']
# ]

def dictAnagrams(group):
    res = {}
    for word in group:
        key = frozenset(Counter(word).items())
        print(key)
        if res.get(key) == None:
            res[key] = []
        res[key].append(word)
    return res.values()


t = time.time()
print(isAnagram('earth', 'heart'))
print(dictAnagrams(groupAnagrams))
print("time:", time.time() - t)
