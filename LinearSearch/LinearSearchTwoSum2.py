def two_sum(nums, target):
    pos = 0
    s = 0
    while s <= len(nums):
        num = nums[pos] + nums[pos + 1]
        if num == target:
            return [pos, pos + 1]
        pos += 1


nums = [2, 3, 4, 5, 6, 7, 9]
target = 16

print("Two Sum WHile: ", two_sum(nums, target))


def two_sum_for(nums, target):
    for pos in range(0, len(nums)):
        num = nums[pos] + nums[pos + 1]
        if num == target:
            return [pos, pos + 1]
        pos += 1


nums = [2, 3, 4, 5, 6, 7, 9]
target = 11

print("two_sum_for: ", two_sum_for(nums, target))
