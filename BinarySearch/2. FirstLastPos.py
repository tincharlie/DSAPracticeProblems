def binary_search(start, end, condition):
    while start <= end:
        mid = (start + end) // 2
        res = condition(mid)
        if res == "Found":
            return mid
        elif res == "Left":
            start = mid - 1
        else:
            end = mid + 1
    return -1


def first_Pos(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return "Left"
            return "Found"
        elif nums[mid] < target:
            return "Right"
        else:
            return "Left"

    return binary_search(0, len(nums) - 1, condition)


def last_Pos(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return "Right"
            return "Found"
        elif nums[mid] < target:
            return "Right"
        else:
            return "Left"

    return binary_search(0, len(nums) - 1, condition)


def firstandlastpos(nums, target):
    return first_Pos(nums, target), last_Pos(nums, target)


cards = [14, 12, 11, 7, 4, 3, 2, 0]
query = 2


print(firstandlastpos(cards, query))