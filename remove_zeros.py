def remove_zeros(a):
    z = None
    for i in range(len(a)):
        if a[i] == 0 and z is None:
            z = i
        elif a[i] != 0 and z is not None:
            a[z], a[i] = a[i], a[z]
            z += 1

    if z is not None:
        del a[z:]
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
