"""
`Problem <https://leetcode-cn.com/problems/subsets-with-duplicates/>`_
--------------------------------------------------------------------------

给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

::

    示例 1：

    输入：nums = [1,2,2]
    输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

    示例 2：

    输入：nums = [0]
    输出：[[],[0]]

    提示：

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10

Tips
------

输出是 ``二维列表``，列表可以是无序，列表的每一项 ``item`` 也是列表，``item`` 也可以是无序。即 ``[3, 4]`` 和 ``[4, 3]`` 是等价的。

* DFS 回溯法:

    - ``nums`` 有重复的元素。那么遇到重复的元素需要判定元素是否处理过。
    -  为了方便判定元素是否处理，先对输入 ``nums`` 进行排序，让重复元素彼此挨着。
    -  回溯决策的时候，如果当前元素的与前一个元素值一样，则可以忽略

* BFS 迭代法


Answer
------

"""

import random
import unittest
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num = random.randint(0, 1)
        d = {
            0: self.dfs,
            1: self.bfs,
        }
        return d[num](nums)

    def dfs(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def backtracking(index, path):
            if index > len(nums):
                return

            ans.append(path[:])
            for i in range(index, len(nums)):
                # 当前元素与前一个元素一样，忽略
                if i > index and nums[i - 1] == nums[i]:
                    continue
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        ans = []
        backtracking(0, [])
        return ans

    def bfs(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        pre_start = 0
        nums.sort()
        for index, item in enumerate(nums):
            size = len(ans)
            # 当前元素和前一个元素一样，只拿出前一轮的集合处理
            if index > 0 and nums[index - 1] == nums[index]:
                start = pre_start
            else:
                start = 0
            for i in range(start, size):
                item = ans[i].copy()
                item.append(nums[index])
                ans.append(item)
            pre_start = size
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 3, 3], [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]),
            ([1, 5, 3, 3],
             [[], [1], [5], [3], [1, 5], [1, 3], [5, 3], [1, 5, 3], [3, 3], [1, 3, 3], [3, 3, 5], [1, 5, 3, 3]]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.subsetsWithDup(nums)
            self.assertTrue(equal(answer, ans))


def equal(nums1: List[List[int]], nums2: List[List[int]]):
    [i.sort() for i in nums1]
    [i.sort() for i in nums2]
    nums1.sort()
    nums2.sort()
    return nums1 == nums2


if __name__ == '__main__':
    unittest.main()
