"""
`Problem <https://leetcode-cn.com/problems/>`_
-----------------------------------------------------------------------------

74. 搜索二维矩阵

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。

该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

::

    示例 1：

    输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    输出：true

    示例 2：

    输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    输出：false

    提示：

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10⁴ <= matrix[i][j], target <= 10⁴

Tips
------

1. 找出目标值所在 row
2. 针对目标 row 进行 二分

O(m*nlogn)

Answer
------

"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0, False),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 100, False),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 30, True),
        ]
        self.s = Solution()

    def test_solution(self):
        for matrix, target, answer in self.test_case:
            ans = self.s.searchMatrix(matrix, target)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
