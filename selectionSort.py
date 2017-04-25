def selectionSort(lst):
    n = len(lst)
    for i in range(n-1):
        m = lst[i]
        idx = 0
        for k in range(i+1, n):
            if lst[k] < m:
                m = lst[k]
                idx = k
        if lst[i] > m:
            lst[i], lst[idx] = lst[idx], lst[i]
    return lst

lst = [5, 3, 7, 2, 6, 4, 0, 9, 1, 8]
print(selectionSort(lst))
