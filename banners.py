from random import randint


def random_nums(_nums):
    while _nums:
        last = len(_nums) - 1
        i = randint(0, last)
        yield (_nums[i])
        if i < last:
            _nums[i] = _nums[last]
        _nums.pop()

nums = list(range(100))
for num in random_nums(nums):
    print(num)
