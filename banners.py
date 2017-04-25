from random import randint


def randomNums(nums):
    while nums:
        last = len(nums) - 1
        i = randint(0, last)
        yield (nums[i])
        if i < last:
            nums[i] = nums[last]
        nums.pop()

# nums = list(range(100))
# for i in randomNums(nums):
#     print(i)
