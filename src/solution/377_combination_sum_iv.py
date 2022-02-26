"""
`Problem <https://leetcode-cn.com/problems/combination-sum-iv/>`_
-----------------------------------------------------------------------------
377. 组合总和IV




Tips
------



Answer
------

"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        def dfs(path):
            nonlocal ans
            sum_ = sum(path)
            if sum_ >= target:
                if sum_ == target:
                    ans += 1
                return
            for item in nums:
                path.append(item)
                dfs(path)
                path.pop()

        ans = 0
        path = []
        dfs(path)
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3], 4, 7),
            ([9], 3, 0)
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, target, answer in self.test_case:
            ans = self.s.combinationSum4(nums, target)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
