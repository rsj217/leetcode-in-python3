"""
`Problem <https://leetcode-cn.com/problems/subarray-sum-equals-k/>`_
-----------------------------------------------------------------------------

560. 和为k的子数组

给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

::

    示例 1：

    输入：nums = [1,1,1], k = 2
    输出：2

    示例 2：

    输入：nums = [1,2,3], k = 3
    输出：2

    提示：

    1 <= nums.length <= 2 * 10⁴
    -1000 <= nums[i] <= 1000
    -10⁷ <= k <= 10⁷


Tips
------

1. 前缀和和twosum思想
2. key=前缀和，val=次数
3. 前缀和为0的初始化

Answer
------

"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = dict()
        dct[0] = 1
        presum = 0
        ans = 0
        for item in nums:
            presum += item
            if presum - k in dct:
                ans += dct[presum - k]
            dct[presum] = dct.get(presum, 0) + 1
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1], 0, 0),
            ([1, 2, 3], 3, 2),
            ([1, 1, 1], 3, 1),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, k, answer in self.test_case:
            ans = self.s.subarraySum(nums, k)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
