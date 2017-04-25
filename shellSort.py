def shell_sort_optimized(lst):
    gap = len(lst) // 2
    while gap:
        for i, el in enumerate(lst):
            while i >= gap and lst[i - gap] > el:
                lst[i] = lst[i - gap]
                i -= gap
            lst[i] = el
        gap = gap // 2


def shell_sort(lst):
    def gap(lst):
        gap = len(lst) // 2
        yield gap
        while gap > 1:
            gap = 1 if gap == 2 else int(round(gap / 2.2))
            yield gap

    for gap in gap(lst):
        print "gap:", gap
        for i in xrange(gap):
            insertion_sort(lst, i, gap)


def insertion_sort(lst, start, gap):
    for i in xrange(start + gap, len(lst)):
        value = lst[i]
        pos = i

        while pos >= gap and lst[pos - gap] > value:
            lst[pos] = lst[pos - gap]
            pos -= gap
        lst[pos] = value


if __name__ == '__main__':
    lst = [54, 64, -15, 26, 81, -5, 93, -33, 47, 10, -52, 33, 17, 22, 77, -24, 31, 44, 7, 55, 20]
    shell_sort(lst)
    # insertion_sort(lst, 0, 1)
    print lst
