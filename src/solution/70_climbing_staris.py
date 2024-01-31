import random
from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        num = random.randint(0, 1)
        d = {
            0: self.solve_dp,
            1: self.solve_recursion,
        }
        return d[num](n)
    
    def solve_dp(self, n: int) -> int:
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n - 1]
    
    def solve_recursion(self, n: int) -> int:
        @lru_cache(None)
        def recursion(n: int) -> int:
            if n == 1:
                return 1
            if n == 2:
                return 2
            return recursion(n - 2) + recursion(n - 1)
        
        return recursion(n)


import unittest


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            (1, 1),
            (2, 2),
            (3, 3),
            (5, 8),
            (8, 34),
            (10, 89),
        
        ]
        self.s = Solution()
    
    def test_solution(self):
        for n, answer in self.test_case:
            ans = self.s.climbStairs(n)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
