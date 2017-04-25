def binary_search(lst, x):
    l = 0
    r = len(lst)
    if r == 0:
        return None
    while r - l > 1:
        m = l + ((r - l) // 2)
        if x > lst[m]:
            l = m
        elif x < lst[m]:
            r = m
        else:
            return m
    return l if x == lst[l] else None

str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = ""
str3 = "a"
str4 = "ab"

print(binary_search(str1, "g"))
