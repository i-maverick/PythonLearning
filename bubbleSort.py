def bubbleSort(lst):
    done = False
    n = len(lst) - 1
    while not done:
        done = True
        for i in range(n):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                done = False
    return lst

lst = [5, 3, 7, 2, 6, 4, 0, 9, 1, 8]
print(bubbleSort(lst))
