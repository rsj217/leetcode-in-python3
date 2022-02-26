"""
`Problem <https://leetcode-cn.com/problems/combination-sum/>`_
-----------------------------------------------------------------------------

39. 组合总和

给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的
所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为 target 的不同组合数少于 150 个。

::

    示例 1：

    输入：candidates = [2,3,6,7], target = 7
    输出：[[2,2,3],[7]]
    解释：
    2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
    7 也是一个候选， 7 = 7 。
    仅有这两种组合。

    示例 2：

    输入: candidates = [2,3,5], target = 8
    输出: [[2,2,2,2],[2,3,3],[3,5]]

    示例 3：

    输入: candidates = [2], target = 1
    输出: []

    提示：

    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    candidate 中的每个元素都 互不相同
    1 <= target <= 500

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
            ([2, 3, 6, 7], 7, [[2,2,3],[7]]),
            ([2, 3, 5], 8,  [[2,2,2,2],[2,3,3],[3,5]]),
            ([2], 1, [])

        ]
        self.s = Solution()

    def test_solution(self):
        for candidates, target, answer in self.test_case:
            ans = self.s.combinationSum(candidates, target)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
