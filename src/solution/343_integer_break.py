"""
`Problem <https://leetcode-cn.com/problems/integer-break/>`_
-------------------------------------------------------------

给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
返回 你可以获得的最大乘积 。

::

    示例 1：

    输入: n = 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1。

    示例 2：

    输入: n = 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

    提示:

    2 <= n <= 58

Tips
------
dp定义：i的下标即入参 n 的整数的最大乘积
初始化：
* dp[0], dp[1] 占位，无意义
* dp[2], dp[3] = 2, 3，这是为后面的做表，不代表当前n=2， n=3的值
* n = 2，3 需要手动校正

递推公式：  f(n) = max(f(2) * f(n-2), f(3) * f(n-3),.... f(n//2), f(n - n//2))

Answer
------

"""


class Solution:
    def integerBreak(self, n: int) -> int:
        assert n > 1, "err"
        if n <= 3:
            return n - 1
        dp = [0] * (n + 1)
        dp[2], dp[3] = 2, 3
        for i in range(4, n + 1):
            dpi = 0
            for j in range(1, i // 2 + 1):
                dpi = max(dpi, dp[j] * dp[i - j])
            dp[i] = dpi
        return dp[n]


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (2, 1),
            (3, 2),
            (4, 4),
            (5, 6),
            (6, 9),
            (7, 12),
            (8, 18),
            (9, 27),
        ]
        self.s = Solution()

    def test_solution(self):
        for n, answer in self.test_case:
            ans = self.s.integerBreak(n)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
