"""
`Problem <https://leetcode-cn.com/problems/combination-sum-ii/>`_
-----------------------------------------------------------------------------

40. 组合总和II

给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。

::

    示例 1:

    输入: candidates =[10,1,2,7,6,1,5], target =8,
    输出:
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]

    示例 2:

    输入: candidates =[2,5,2,1,2], target =5,
    输出:
    [
    [1,2,2],
    [5]
    ]

    提示:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

Tips
------

回溯法
1.递归基，path的和大于target
2.解：path的和等于 target
3.树遍历：每次提出上次遍历的根节点

Answer
------

"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates: List[int], target: int, index: int, path: List[int], ans: List[List[int]]):
            sum_ = sum(path)
            if sum_ >= target:
                if sum_ == target:
                    ans.append(path[:])
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(candidates, target, i, path, ans)
                path.pop()

        ans = []
        path = []
        index = 0
        dfs(candidates, target, index, path, ans)
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            ([2], 1, [])

        ]
        self.s = Solution()

    def test_solution(self):
        for candidates, target, answer in self.test_case:
            ans = self.s.combinationSum(candidates, target)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()