"""
`Problem <https://leetcode-cn.com/problems/minimum-size-subarray-sum/>`_
-----------------------------------------------------------------------------

209. 长度最小的子数组

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长
度。如果不存在符合条件的子数组，返回 0 。



示例 1：


输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。


示例 2：


输入：target = 4, nums = [1,4,4]
输出：1


示例 3：


输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0




提示：


1 <= target <= 10⁹
1 <= nums.length <= 10⁵
1 <= nums[i] <= 10⁵




进阶：


如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。


Tips
------

题解

Answer
------

"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        lo, hi = 0, 0
        win_sum = 0
        while hi < len(nums):
            win_sum += nums[hi]
            hi += 1

            while win_sum >= target:
                ans = min(ans, hi - lo)
                win_sum -= nums[lo]
                lo += 1
        return 0 if ans == len(nums) + 1 else ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (4, [1, 4, 4], 1),
            (7, [2, 3, 1, 2, 4, 3], 2)
        ]
        self.s = Solution()

    def test_solution(self):
        for target, nums, answer in self.test_case:
            ans = self.s.minSubArrayLen(target, nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
