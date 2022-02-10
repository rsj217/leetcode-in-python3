"""
`Problem <https://leetcode-cn.com/problems/longest-increasing-subsequence/>`_
-------------------------------------------------------------------------------

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序
列。

::

    示例 1：

    输入：nums = [10,9,2,5,3,7,101,18]
    输出：4
    解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

    示例 2：

    输入：nums = [0,1,0,3,2,3]
    输出：4

    示例 3：

    输入：nums = [7,7,7,7,7,7,7]
    输出：1

    提示：

    1 <= nums.length <= 2500
    -10⁴ <= nums[i] <= 10⁴

    进阶：

    你可以设计时间复杂度为 O(n²) 的解决方案吗？
    你能将算法的时间复杂度降低到 O(n log(n)) 吗?


Tips
------

::

    dp[i] 表示 长度为 i 的 最大上升子序列长度

    f(n) = max(f(i)) + 1  a[i] < a[n]
           max(f(i))


Answer
--------
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
