"""
`Problem <https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/>`_
-------------------------------------------------------------------------------------

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

::

   示例 1：

   输入：nums = [1,1,2]
   输出：2, nums = [1,2]
   解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
   示例 2：

   输入：nums = [0,0,1,1,1,2,2,3,3,4]
   输出：5, nums = [0,1,2,3,4]
   解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素


Tips
------

快排思想

Answer
--------

"""
from typing import List
import unittest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return len(nums)

        j = 0
        for i in range(1, len(nums)):
            if nums[j] < nums[i]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([2, 2, 3, 3], 2),
            ([0, 1, 2, 2, 3, 4], 5),
            ([0,0,1,1,1,2,2,3,3,4], 5),
            ([0], 1),
            ([], 0),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.removeDuplicates(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
