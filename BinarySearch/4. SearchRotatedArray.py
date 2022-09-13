def searchRotatedArr(arr, n, target):
    s, e = 0, n - 1
    mid = (s + e) // 2
    while s <= e:
        if target == arr[mid]:
            return mid
        # Search start sorted portion
        if arr[s] <= arr[mid]:
            if target > arr[mid]:
                s = mid + 1
            elif target < arr[s]:
                s = mid + 1
            else:
                e = mid - 1
        else:
            if target < arr[mid]:
                e = mid - 1
            elif target > arr[e]:
                e = mid - 1
            else:
                s = mid + 1
        mid = (s + e) // 2
    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
target = 7
n = 8

print(searchRotatedArr(arr, n, target))
