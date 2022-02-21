"""
`Problem <https://leetcode-cn.com/problems/max-consecutive-ones//>`_
-----------------------------------------------------------------------------

给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

::

    示例 1：

    输入：nums = [1,1,0,1,1,1]
    输出：3
    解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
    示例 2:

    输入：nums = [1,0,1,1,0,1]
    输出：2

    提示：

    1 <= nums.length <= 105
    nums[i]不是0就是1.

Tips
------

1. 双指针
2. 状态机

Answer
------

"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        i, j = 0, 0
        while i < len(nums):
            if nums[i] == 1:
                i += 1
            else:
                ans = max(ans, i - j)
                i += 1
                j = i
        ans = max(ans, i - j)
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 1], 2),
            ([1, 1, 0, 1, 1, 1], 3)
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.findMaxConsecutiveOnes(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
