"""
`Problem <https://leetcode.cn/problems/target-sum/description///>`_
-----------------------------------------------------------------------------
给你一个非负整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

::

    示例 1：

    输入：nums = [1,1,1,1,1], target = 3
    输出：5
    解释：一共有 5 种方法让最终目标和为 3 。
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3
    
    示例 2：

    输入：nums = [1], target = 1
    输出：1

    提示：

    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000

Tips
------

1. 递归动态规划+记忆化搜索

Answer
------

"""
import random
from typing import List
from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        num = random.randint(0, 1)
        d = {
            0: self.solve1,
            1: self.solve2,
        }
        return d[num](nums, target)
    
    def solve1(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(idx: int, target_sum: int) -> int:
            if len(nums) <= idx:
                return 1 if target_sum == 0 else 0
            ans_plus = dfs(idx + 1, target_sum + nums[idx])
            ans_sub = dfs(idx + 1, target_sum - nums[idx])
            return ans_plus + ans_sub
        
        return dfs(0, target)
    
    def solve2(self, nums: List[int], target: int) -> int:
        def dfs(idx: int, target_sum: int) -> int:
            if len(nums) <= idx:
                return 1 if target_sum == 0 else 0
            if dp.get(f"{idx}-{target_sum}") != None:
                return dp.get(f"{idx}-{target_sum}")
            
            ans1 = dfs(idx + 1, target_sum + nums[idx])
            ans2 = dfs(idx + 1, target_sum - nums[idx])
            dp[f"{idx}-{target_sum}"] = ans1 + ans2
            return dp[f"{idx}-{target_sum}"]
        
        dp = dict()
        return dfs(0, target)


import unittest


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            ([1, 1, 1, 1, 1], 3, 5),
            ([1], 1, 1),
            ([43, 9, 26, 24, 39, 40, 20, 11, 18, 13, 14, 30, 48, 47, 37, 24, 32, 32, 2, 26], 47, 5844)
        ]
        self.s = Solution()
    
    def test_solution(self):
        for nums, target, answer in self.test_case:
            ans = self.s.findTargetSumWays(nums, target)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
