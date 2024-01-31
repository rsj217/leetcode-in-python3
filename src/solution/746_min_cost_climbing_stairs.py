import unittest
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        return min(dp[-1], dp[-2])


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            ([10, 15, 20], 15),
            ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ]
        self.s = Solution()
    
    def test_solution(self):
        for cost, answer in self.test_case:
            ans = self.s.minCostClimbingStairs(cost)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
