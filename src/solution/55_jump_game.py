"""
`Problem <https://leetcode.cn/problems/number-of-common-factors/>`_
--------------------------------------------------------
55. 跳跃游戏

给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

::

    示例 1：

    输入：nums = [2,3,1,1,4]
    输出：true
    解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
    
    示例 2：

    输入：nums = [3,2,1,0,4]
    输出：false
    解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

    提示：

    1 <= nums.length <= 104
    0 <= nums[i] <= 105

Tips
------

斐波那契式动态规划，f(n) 需要 f(n-1) f(n-2) 的关系

dfs 函数定义：返回剩余 nums 的能否到达最后一个索引

Answer
------

"""
import random
from typing import List

from functools import lru_cache


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(idx: int) -> bool:
            if len(nums) - 1 <= idx:
                return True
            
            curr = nums[idx]
            for i in range(1, curr + 1):
                if dfs(idx + i):
                    return True
            return False
        
        return dfs(0)


import unittest


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            ([2, 3, 1, 1, 4], True),
            ([3, 2, 1, 0, 4], False),
            ([0], True),
            ([2, 0, 0], True),
            ([2, 3, 0, 1, 4], True),
            ([2, 1], True),
        ]
        self.s = Solution()
    
    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.canJump(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
