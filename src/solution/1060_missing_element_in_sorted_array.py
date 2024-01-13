"""
`Problem <https://leetcode-cn.com/problems/>`_
-----------------------------------------------------------------------------

题目描述

::

    示例 1：

    入：nums = [2,7,11,15], target = 9
    出：[0,1]
    释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。



    提示：

    2 <= nums.length <= 103


Tips
------

比对  nums[i]  和 nums[i+1] 之间的缺失的个数 d， 如果 d < k , 则从 k 中剔除d， 即 k = k-d，然后以 nums[i+1] 为数组的第一个数，递归执行。
如果 k <= d, 即表示d中包含缺失的数字，返回  nums[i]+k 即可。
递归基处理，当元素是最后一个元素的时候，还没有到k，需要使用 nums[len(nums)-1] + k，即以最后一个元素为第一个元素

1. 递归
2. 迭代

Answer
------

"""

from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        assert 1 <= k <= 10 ** 8
        return self.missingElement_1(nums, k)

    def missingElement_1(self, nums: List[int], k: int) -> int:
        def helper(nums: List[int], k: int, index: int) -> int:
            if index >= len(nums) - 1:
                return nums[len(nums) - 1] + k
            d = nums[index + 1] - nums[index] - 1
            if d < k:
                return helper(nums, k - d, index + 1)
            return nums[index] + k

        return helper(nums, k, 0)

    def missingElement_2(self, nums: List[int], k: int) -> int:
        for i in range(len(nums) - 1):
            d = nums[i + 1] - nums[i] - 1
            if d < k:
                k -= d
            else:
                return nums[i] + k
        return nums[len(nums) - 1] + k


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([4, 7, 9, 10], 1, 5),
            ([4, 7, 9, 10], 2, 6),
            ([4, 7, 9, 10], 3, 8),
            ([4, 7, 9, 10], 3, 8),
            ([1, 2, 4], 3, 6),
            ([1], 3, 4),
            ([0], 3, 3),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, k, answer in self.test_case:
            ans = self.s.missingElement(nums, k)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
