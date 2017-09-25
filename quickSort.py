def qsort(lst):
    if not lst:
        return []
    piv = (lst[0] + lst[len(lst) // 2] + lst[-1]) // 3
    return qsort([x for x in lst if x < piv])\
        + [x for x in lst if x == piv]\
        + qsort([x for x in lst if x > piv])

lst = [54, 26, 93, 17, 77, 31, 44, 55, 20, 10, 22, 101, 546, -15, 23, 66, -55, -17, 0, 5, 223]
print(qsort(lst))
