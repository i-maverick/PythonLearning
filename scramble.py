from collections import defaultdict


def scramble(name):
    array = []
    frequency = defaultdict(int)

    def sort_by_frequency(char):
        return frequency[char]

    for c in name:
        array.append(c)
        frequency[c] += 1
    array.sort(key=sort_by_frequency, reverse=True)
    return "".join(array)

print(scramble("Justice League"))
