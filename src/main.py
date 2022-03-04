matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13


def aaa(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    row = m
    for i in range(m):
        if target < matrix[i][n - 1]:
            row = i
            break
        elif target == matrix[i][n - 1]:
            return True

    if row == m:
        return False
    lo, hi = 0, n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if target < matrix[row][mid]:
            hi = mid
        elif matrix[row][mid] < target:
            lo = mid + 1
        else:
            return True
    return False


ans = aaa(matrix, target)
print(ans)
