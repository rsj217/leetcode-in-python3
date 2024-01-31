"""
`Problem <https://leetcode.cn/problems/number-of-common-factors/>`_
--------------------------------------------------------
2427. 公因子的数目

给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。

如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。

::

    示例 1：

    输入：a = 12, b = 6
    输出：4
    解释：12 和 6 的公因子是 1、2、3、6 。
    示例 2：

    输入：a = 25, b = 30
    输出：2
    解释：25 和 30 的公因子是 1、5 。


    提示：

    1 <= a, b <= 10007

Tips
------

Answer
------

"""
import random
from typing import List


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        seq = random.randint(1, 2)
        fname = f"solve_{seq}"
        f = getattr(self, fname)
        print(f.__name__)
        return f(a, b)
    
    def solve_1(self, a: int, b: int) -> int:
        t = a if a <= b else b
        
        ans = 0
        for i in range(1, t + 1):
            if (a % i == 0) and (b % i == 0):
                ans += 1
        return ans
    
    def solve_2(self, a: int, b: int) -> int:
        def search(n: int) -> int:
            if n == t + 1:
                return 0
            c = 1 if (a % n == 0 and b % n == 0) else 0
            return c + search(n + 1)
        
        t = a if a <= b else b
        return search(1)


import unittest


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            (12, 6, 4),
            (25, 30, 2),
        ]
        self.s = Solution()
    
    def test_solution(self):
        for a, b, answer in self.test_case:
            ans = self.s.commonFactors(a, b)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
