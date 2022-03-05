"""
`Problem <https://leetcode-cn.com/problems/minimum-path-sum>`_
----------------------------------------------------------------

给定一个包含非负整数的 m * n网格grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。


.. image:: ../../img/64.jpeg

::

    示例 1：

    输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
    输出：7
    解释：因为路径 1→3→1→1→1 的总和最小。
    示例 2：

    输入：grid = [[1,2,3],[4,5,6]]
    输出：12

    提示：

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100

Tips
------

    递推公式:
    f(m, n) = min(f(m-1, n), f(m, n-1)) + g(m, n)

+------------+------------+-----------+------------+
|            |  0         | 1         | 2          |
+============+============+===========+============+
| 0          |  1         | 4         | 5          |
+------------+------------+-----------+------------+
| 1          |  2         | 7         | 6          |
+------------+------------+-----------+------------+
| 2          |  6         | 8         | 7          |
+------------+------------+-----------+------------+


Answer
------

"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for i in range(m)]
        for x in range(n):
            if x == 0:
                dp[0][0] = grid[0][0]
            else:
                dp[0][x] = dp[0][x - 1] + grid[0][x]

        for y in range(m):
            if y == 0:
                dp[0][0] = grid[0][0]
            else:
                dp[y][0] = dp[y - 1][0] + grid[y][0]

        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = min(dp[y - 1][x], dp[y][x - 1]) + grid[y][x]

        return dp[m - 1][n - 1]


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
            ([[1, 2, 3], [4, 5, 6]], 12)
        ]
        self.s = Solution()

    def test_solution(self):
        for grid, answer in self.test_case:
            ans = self.s.minPathSum(grid)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
