"""
`Problem <https://leetcode-cn.com/problems/permutations>`_
-----------------------------------------------------------------------------

46. 全排列

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

::

    示例 1：

    输入：nums = [1,2,3]
    输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    示例 2：

    输入：nums = [0,1]
    输出：[[0,1],[1,0]]
    示例 3：

    输入：nums = [1]
    输出：[[1]]

    提示：

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    nums 中的所有整数 互不相同


Tips
------

回溯法
1. 遍历数组
2. 记录已遍历路径

Answer
------

"""
import unittest
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums: List[int], visited: List[int], path: List[int], ans: List[List[int]]):
            assert 1 <= len(nums) <= 6, "nums err"
            if len(nums) == len(path):
                ans.append(path[:])
                return
            for item in nums:
                if item in visited:
                    continue
                visited.append(item)
                path.append(item)
                dfs(nums, visited, path, ans)
                path.pop()
                visited.pop()

        visited = []
        path = []
        ans = []
        dfs(nums, visited, path, ans)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1], [[1]]),
            ([0, 1], [[0, 1], [1, 0]]),
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.permute(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
