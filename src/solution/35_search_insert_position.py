"""
`Problem <https://leetcode-cn.com/problems/search-insert-position/>`_
-----------------------------------------------------------------------

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

::

    示例 1:

    输入: [1,3,5,6], 5
    输出: 2


    示例 2:

    输入: [1,3,5,6], 2
    输出: 1


    示例 3:

    输入: [1,3,5,6], 7
    输出: 4


    示例 4:

    输入: [1,3,5,6], 0
    输出: 0

Tips
------



Answer
------

"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:  # 绝对小于，右半边
                lo = mid + 1
            else:  # target <= nums[mid]
                hi = mid
        return hi


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 3, 4, 6], 7, 4),
            ([4, 5, 5, 5], 5, 1),
            ([1, 2, 2, 3, 4, 5], 2, 1),
        ]
        self.s = Solution()

    def test_solution(self):
        for item, target, answer in self.test_case:
            ans = self.s.searchInsert(item, target)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
