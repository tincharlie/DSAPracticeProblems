def mountainPeak(arr):
    s = 0
    e = len(arr) - 1

    while s < e:
        mid = (s + e) // 2
        if arr[mid] < arr[mid + 1]:
            s = mid + 1
        else:
            e = mid - 1

    return s


arr = [2, 4, 6, 7, 8, 9, 5, 4, 1]

print("Mountain Peak index array is:", mountainPeak(arr))
