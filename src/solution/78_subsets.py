"""
`Problem <https://leetcode-cn.com/problems/subsets/>`_
-------------------------------------------------------------

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

::

    示例:

    输入: n = 4, k = 2

    输出:

    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]

Tips
------

输出是 ``二维列表``，列表可以是无序，列表的每一项 ``item`` 也是列表，``item`` 也可以是无序。即 ``[3, 4]`` 和 ``[4, 3]`` 是等价的。

* DFS 回溯法
* BFS 迭代法


Answer
------

"""
import random
import unittest
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        num = random.randint(0, 1)
        d = {
            0: self.dfs,
            1: self.bfs,
        }
        return d[num](nums)

    def dfs(self, nums: List[int]) -> List[List[int]]:
        def backtracking(index, path):
            if index > len(nums):
                return

            ans.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        ans = []
        backtracking(0, [])
        return ans

    def bfs(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            size = len(ans)
            for i in range(size):
                item = ans[i].copy()
                item.append(num)
                ans.append(item)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 3], [[], [1], [1, 3], [3]]),
            ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
            ([1, 5, 3], [[], [1], [1, 5], [1, 5, 3], [1, 3], [5], [5, 3], [3]]),

        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.subsets(nums)
            self.assertTrue(equal(answer, ans))


def equal(nums1: List[List[int]], nums2: List[List[int]]):
    nums1.sort()
    nums2.sort()
    return nums1 == nums2


if __name__ == '__main__':
    unittest.main()
