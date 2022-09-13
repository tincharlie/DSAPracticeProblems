def searchInsert(arr, target):
    n = len(arr)
    s, e = 0, n - 1
    while s <= e:
        mid = (s + e) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            s = mid + 1
        elif target < arr[mid]:
            e = mid - 1
    return s

arr=[1, 3, 5, 7, 9, 11]
target = 9

print(searchInsert(arr, target))