def scramble(name):
    array = []
    frequency = {}

    def sort_by_frequency(char):
        return frequency[char]

    for c in name:
        array.append(c)
        frequency[c] = frequency[c] + 1 if c in frequency else 1
    array.sort(key=sort_by_frequency, reverse=True)
    return "".join(array)

print(scramble("Justice League"))
