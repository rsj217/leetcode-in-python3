"""
`Problem <https://leetcode-cn.com/problems/unique-paths-ii/>`_
---------------------------------------------------------------------

63. 不同路径 II

一个机器人位于一个m x n网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。

.. image:: ../../img/63-1.jpeg

::

    示例 1：

    输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    输出：2
    解释：3x3 网格的正中间有一个障碍物。
    从左上角到右下角一共有 2 条不同的路径：
    1. 向右 -> 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右 -> 向右


.. image:: ../../img/63-2.jpeg

::

    示例 2：

    输入：obstacleGrid = [[0,1],[0,0]]
    输出：1

    提示：

    m ==obstacleGrid.length
    n ==obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] 为 0 或 1


Tips
------

1. 障碍物的格子是0，
2. 最上面的行和最左边的列，只要障碍物，当前行或当前列后面的格子都是 0
3. 递推公式：  f(m, n) = f(m-1, n) + f(m, n-1)

Answer
------

"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        # 最上面一行
        for x in range(n):
            if obstacleGrid[0][x] == 1:
                dp[0][x] = 0
            else:
                dp[0][x] = 1 if x == 0 else dp[0][x - 1]

        # 最左边一行
        for y in range(m):
            if obstacleGrid[y][0] == 1:
                dp[y][0] = 0
            else:
                dp[y][0] = 1 if y == 0 else dp[y - 1][0]

        # 剩余行
        for y in range(1, m):
            for x in range(1, n):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                else:
                    dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
        return dp[m - 1][n - 1]


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([[0, 1, 0], [0, 1, 0], [0, 0, 0]], 1),
            ([[0, 1, 0], [1, 0, 0], [0, 0, 0]], 0),
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
            ([[0, 1], [0, 0]], 1),
        ]
        self.s = Solution()

    def test_solution(self):
        for obstacleGrid, answer in self.test_case:
            ans = self.s.uniquePathsWithObstacles(obstacleGrid)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
