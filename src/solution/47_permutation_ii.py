"""
`Problem <https://leetcode-cn.com/problems/permutations-ii>`_
-----------------------------------------------------------------------------

47. 全排列II

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

::

    示例 1：

    输入：nums = [1,1,2]
    输出：
    [[1,1,2],
    [1,2,1],
    [2,1,1]]

    示例 2：

    输入：nums = [1,2,3]
    输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    提示：

    1 <= nums.length <= 8
    -10 <= nums[i] <= 10


Tips
------

1. hash记录元素个数
2. 去重
3. 回溯遍历树

Answer
------

"""

from typing import List, Dict


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums: List[int], nums_size: int, nums_dct: Dict[int, int], visited_dct: Dict[int, int], path: List[int],
                ans: List[List[int]]):
            if nums_size == len(path):
                ans.append(path[:])
                return

            for item in nums:
                if visited_dct.get(item, 0) >= nums_dct[item]:
                    continue

                visited_dct[item] = visited_dct.get(item, 0) + 1
                path.append(item)
                dfs(nums, nums_size, nums_dct, visited_dct, path, ans)
                path.pop()
                visited_dct[item] = visited_dct[item] - 1

        assert 1 <= len(nums) <= 8, "nums err"

        nums_dct = dict()
        for item in nums:
            nums_dct[item] = nums_dct.get(item, 0) + 1

        nums_size = len(nums)
        nums = list(set(nums))
        visited_dct = dict()
        path = []
        ans = []
        dfs(nums, nums_size, nums_dct, visited_dct, path, ans)
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            ([1], [[1]]),
            ([3, 3, 6, 6, 9],
             [[9, 3, 3, 6, 6], [9, 3, 6, 3, 6], [9, 3, 6, 6, 3], [9, 6, 3, 3, 6], [9, 6, 3, 6, 3], [9, 6, 6, 3, 3],
              [3, 9, 3, 6, 6], [3, 9, 6, 3, 6], [3, 9, 6, 6, 3], [3, 3, 9, 6, 6], [3, 3, 6, 9, 6], [3, 3, 6, 6, 9],
              [3, 6, 9, 3, 6], [3, 6, 9, 6, 3], [3, 6, 3, 9, 6], [3, 6, 3, 6, 9], [3, 6, 6, 9, 3], [3, 6, 6, 3, 9],
              [6, 9, 3, 3, 6], [6, 9, 3, 6, 3], [6, 9, 6, 3, 3], [6, 3, 9, 3, 6], [6, 3, 9, 6, 3], [6, 3, 3, 9, 6],
              [6, 3, 3, 6, 9], [6, 3, 6, 9, 3], [6, 3, 6, 3, 9], [6, 6, 9, 3, 3], [6, 6, 3, 9, 3], [6, 6, 3, 3, 9]]
             ),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.permuteUnique(nums)
            self.assertListEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
