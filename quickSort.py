def qsort(_lst):
    if not lst:
        return []
    return qsort([x for x in lst if x < lst[0]])\
        + [x for x in lst if x == lst[0]]\
        + qsort([x for x in lst if x > lst[0]])

lst = [54, 26, 93, 17, 77, 31, 44, 55, 20, 10, 22, 101, 546, -15, 23, 66, -55, -17, 0, 5, 223]
qsort(lst)
print lst
