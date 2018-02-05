def remove_zeros(a):
    pos = None
    for i, n in enumerate(a):
        if n == 0 and pos is None:
            pos = i
        elif n != 0 and pos is not None:
            a[pos], n = n, a[pos]
            pos += 1

    if pos is not None:
        del a[pos:]
    return a


assert remove_zeros([0, 1, 0, 0, 3, 4, 0, 5, 2, 1, 0, 7, 0]) == [1, 3, 4, 5, 2, 1, 7]
assert remove_zeros([1, 3, 0, 4, 0, 2, 5, 0]) == [1, 3, 4, 2, 5]
assert remove_zeros([]) == []
assert remove_zeros([1]) == [1]
assert remove_zeros([0]) == []
assert remove_zeros([1, 0]) == [1]
assert remove_zeros([0, 1]) == [1]
assert remove_zeros([1, 0, 0, 0]) == [1]
assert remove_zeros([0, 0, 0, 1]) == [1]
assert remove_zeros([0, 0, 0]) == []
assert remove_zeros([1, 1, 1]) == [1, 1, 1]
