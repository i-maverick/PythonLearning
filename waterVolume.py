def calc_volume(land):
    volume = 0
    left = 0
    right = len(land) - 1
    left_max = 0
    right_max = 0
    while left < right:
        if land[left] > left_max:
            left_max = land[left]
        if land[right] > right_max:
            right_max = land[right]

        if left_max < right_max:
            left += 1
            if land[left] < left_max:
                volume += (left_max - land[left])
        else:
            right -= 1
            if land[right] < right_max:
                volume += (right_max - land[right])

    return volume


# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

land1 = [1, 2, 4, 6, 1, 2, 1, 3, 8, 2, 3, 7, 4]
print(calc_volume(land1))
