from collections import Counter


def dict_word(word):
    d = {}
    for i in word:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def is_anagram(first, second):
    return Counter(first) == Counter(second)


groupAnagrams = ['сон', 'нос', 'сорт', 'трос', 'торт', 'рост']


# [
# ['сон', 'нос'],
# ['сорт', 'трос', 'рост'],
# ['торт']
# ]

def dict_anagrams(group):
    res = {}
    for word in group:
        key = frozenset(Counter(word).items())
        print(key)
        if key not in res:
            res[key] = []
        res[key].append(word)
    return res.values()


print(is_anagram('earth', 'heart'))
print(dict_anagrams(groupAnagrams))
