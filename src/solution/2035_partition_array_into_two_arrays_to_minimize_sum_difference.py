"""
`Problem <https://leetcode.cn/problems/partition-array-into-two-arrays-to-minimize-sum-difference>`_
--------------------------------------------------------
2035. 将数组分成两个数组并最小化数组和的差

给你一个长度为 2 * n 的整数数组。你需要将 nums 分成 两个 长度为 n 的数组，分别求出两个数组的和，并 最小化 两个数组和之 差的绝对值 。nums 中每个元素都需要放入两个数组之一。

请你返回 最小 的数组和之差。

::

    示例 1：

    输入：nums = [3,9,7,3]
    输出：2
    解释：最优分组方案是分成 [3,9] 和 [7,3] 。
    数组和之差的绝对值为 abs((3 + 9) - (7 + 3)) = 2 。
    
    示例 2：

    输入：nums = [-36,36]
    输出：72
    解释：最优分组方案是分成 [-36] 和 [36] 。
    数组和之差的绝对值为 abs((-36) - (36)) = 72 。
    
    示例 3：

    输入：nums = [2,-1,0,4,-2,-9]
    输出：0
    解释：最优分组方案是分成 [2,4,-9] 和 [-1,0,-2] 。
    数组和之差的绝对值为 abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0 。

    提示：

    1 <= n <= 15
    nums.length == 2 * n
    -107 <= nums[i] <= 107

Tips
------

Answer
------

"""

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        pass
        # def dfs(idx: int, sum1: int, sum2: int) -> int:
        #     if idx == len(nums):
        #         return abs(sum1 - sum2)
        #
        #     curr = nums[idx]
        #     diff1 = dfs(idx + 1, sum1 + curr, sum2)
        #     diff2 = dfs(idx + 1, sum1, sum2 + curr)
        #     return min(diff1, diff2)
        #
        # return dfs(0, 0, 0)


import unittest


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            # ([3, 9, 7, 3], 2),
            ([-36, 36], 72),
            # ([2, -1, 0, 4, -2, -9], 0),
            # ([1, 2, 3, 9], 3),
            # ([1, 2, 7, 1, 5], 0),
            # ([1, 3, 100, 4], 92),
        ]
        self.s = Solution()
    
    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.minimumDifference(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
