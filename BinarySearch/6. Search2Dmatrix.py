def searchMatrix(matrix, target):
    Rows, Cols = len(matrix), len(matrix[0])
    First, Last = 0, Rows - 1
    while First <= Last:
        row = (First + Last) // 2
        print("MIdROW infirst Place", row)

        if target > matrix[row][-1]:
            """
            MidRow ka last element chhota hai target se toh MidRow ka increment krenge
            """
            First = row + 1
        elif target < matrix[row][0]:
            Last = row - 1
        else:
            break

    if not First <= Last:
        return False

    row = (Last + First) // 2
    print("MIdROW inSecond Place", row)
    s = 0
    e = Cols - 1
    while s <= e:
        m = (s + e) // 2
        print("Row and Mid Element", row, m)
        if target > matrix[row][m]:
            s = m + 1
        elif target < matrix[row][m]:
            e = m - 1
        else:
            return True, row, m
    return False


a = [[1, 3, 5, 7, 8, 9], [10, 11, 15, 16, 17], [20, 21, 23, 24, 25, 27], [30, 31, 32, 33, 34, 35]]
t = 35

print(searchMatrix(a, t))

