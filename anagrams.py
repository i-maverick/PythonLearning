from collections import Counter
from collections import defaultdict


def dict_word(word):
    d = defaultdict(int)
    for i in word:
        d[i] += 1
    return d


def is_anagram(first, second):
    return sorted(first) == sorted(second)


def is_anagram_cnt(first, second):
    return Counter(first) == Counter(second)


def is_anagram_pass(s1, s2):
    if len(s1) != len(s2):
        return False
    for a in s1:
        if s1.count(a) != s2.count(a):
            return False
    return True


def make_key(word):
    return ''.join(sorted(word))


def group_anagrams(group):
    result = defaultdict(list)
    for word in group:
        result[make_key(word)].append(word)
    for rec in result:
        print(result[rec])


groupAnagrams = ['сон', 'нос', 'сорт', 'трос', 'торт', 'рост', 'торот']

# [
# ['сон', 'нос'],
# ['сорт', 'трос', 'рост'],
# ['торт']
# ]


print(is_anagram('earth', 'heart'))
print(group_anagrams(groupAnagrams))
