"""
`Problem <https://leetcode-cn.com/problems/remove-element/submissions/>`_
-------------------------------------------------------------------------------------

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

::

   示例 1：

   输入：nums = [3,2,2,3], val = 3
   输出：2, nums = [2,2]
   解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

   示例 2：

   输入：nums = [0,1,2,2,3,0,4,2], val = 2
   输出：5, nums = [0,1,4,0,3]
   解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。

Tips
------


Answer
--------
"""
from typing import List
import unittest


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return self.fast_slow_pointer(nums, val)

    def fast_slow_pointer(self, nums: List[int], val: int):
        j, i = 0, 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

    def collision_pointer(self, nums: List[int], val: int):
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return r + 1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([3, 2, 2, 3], 3, 2),
            ([3, 2, 2, 3], 2, 2),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
            ([0], 1, 1),
            ([0], 0, 0),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, val, answer in self.test_case:
            ans = self.s.removeElement(nums, val)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
