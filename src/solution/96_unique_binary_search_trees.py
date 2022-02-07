"""
`Problem <https://leetcode-cn.com/problems/unique-binary-search-trees/>`_
--------------------------------------------------------------------------

96.不同的二叉搜索树

给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

.. image:: ../../img/96.jpeg

::

    示例 1：

    输入：n = 3
    输出：5

    示例 2：

    输入：n = 1
    输出：1

    提示：

    1 <= n <= 19

Tips
------




Answer
------

"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # dp[0] 无实际意义
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (1, 1),
            (2, 2),
            (3, 5),
            (4, 14),
            (19, 1767263190)
        ]
        self.s = Solution()

    def test_solution(self):
        for n, answer in self.test_case:
            ans = self.s.numTrees(n)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
