"""

dp[i] 表示 长度为 i 的 最大上升子序列长度
f(n) = max(f(i)) + 1  a[i] < a[n]
       max(f(i))

"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([7, 7, 7, 7, 7, 7, 7], 1),
            ([4, 10, 4, 3, 8, 9], 3),
            ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.lengthOfLIS(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
