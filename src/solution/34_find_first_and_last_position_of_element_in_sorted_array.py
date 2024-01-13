"""
`Problem <https://leetcode-cn.com/problems/>`_
-----------------------------------------------------------------------------

34. 在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

::

    示例 1：

    输入：nums = [5,7,7,8,8,10], target = 8
    输出：[3,4]

    示例 2：

    输入：nums = [5,7,7,8,8,10], target = 6
    输出：[-1,-1]

    示例 3：

    输入：nums = [], target = 0
    输出：[-1,-1]

    提示：

    0 <= nums.length <= 10⁵
    -10⁹ <= nums[i] <= 10⁹
    nums 是一个非递减数组
    -10⁹ <= target <= 10⁹

Tips
------


Answer
------

"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 0:
            return [-1, -1]
        # find left
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target <= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        if len(nums) <= lo or nums[lo] != target:
            # 找不到元素
            return [-1, -1]
        left = lo

        # find right
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return [left, lo - 1]


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([], 3, [-1, -1]),
            ([1], 3, [-1, -1]),
            ([4], 3, [-1, -1]),
            ([3], 3, [0, 0]),
            ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
            ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, target, answer in self.test_case:
            ans = self.s.searchRange(nums, target)
            self.assertListEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
