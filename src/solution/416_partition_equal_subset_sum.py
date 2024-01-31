"""
`Problem <https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/>`_
-------------------------------------------------------------------------------------

416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

::

示例 1：

    输入：nums = [1,5,11,5]
    输出：true
    解释：数组可以分割成 [1, 5, 5] 和 [11] 。
    
    示例 2：
    输入：nums = [1,2,3,5]
    输出：false
    解释：数组不能分割成两个元素和相等的子集。

    提示：
    1 <= nums.length <= 200
    1 <= nums[i] <= 100
    
Tips
------

动态规划
Assume if S represents the total sum of all the given numbers, then the two equal subsets must have a sum equal to S/2.
This essentially transforms our problem to: "Find a subset of the given numbers that has a total sum of S/2".

每个元素可以选和不选，一种情况是选了，那么就求剩余元素的和；另外一种情况是没有选，求剩余元素的和

Answer
------

"""

from functools import lru_cache
from typing import List


class Solution:
    
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(idx: int, curr_sum: int) -> bool:
            if curr_sum == half_sum:
                return True
            
            if idx == len(nums):
                return False
            
            curr = nums[idx]
            if curr + curr_sum <= half_sum:
                if dfs(idx + 1, curr + curr_sum):
                    return True
            return dfs(idx + 1, curr_sum)
        
        assert 1 <= len(nums) <= 200
        nums_sum = sum(nums)
        half_sum = nums_sum // 2
        if nums_sum % 2 != 0:
            return False
        
        return dfs(0, 0)


import unittest


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            ([1, 5, 11, 5], True),
            ([1, 2, 3, 5], False),
            ([14, 9, 8, 4, 3, 2], True),
            ([1, 2, 3, 4], True),
            ([1, 1, 3, 4, 7], True),
            ([2, 3, 4, 6], False),
        ]
        self.s = Solution()
    
    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.canPartition(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
