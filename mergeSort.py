def merge_sort(lst):
    if len(lst) < 2:
        return lst
    res = []
    mid = len(lst) // 2
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])

    while len(l) > 0 and len(r) > 0:
        if l[0] < r[0]:
            res.append(l.pop(0))
        else:
            res.append(r.pop(0))
    res.extend(l + r)
    return res

lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print merge_sort(lst)
