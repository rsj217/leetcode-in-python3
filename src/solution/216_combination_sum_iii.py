"""
`Problem <https://leetcode-cn.com/problems/combination-sum-iii/>`_
-----------------------------------------------------------------------------
216. 组合总和III

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
说明：
所有数字都是正整数。
解集不能包含重复的组合。

::

    示例 1:

    输入: k = 3, n = 7
    输出: [[1,2,4]]


    示例 2:

    输入: k = 3, n = 9
    输出: [[1,2,6], [1,3,5], [2,3,4]]



Tips
------



Answer
------

"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(k, n, index, path):
            if len(path) == k:
                if sum(path) == n:
                    ans.append(path[:])
                return
            for i in range(index, 10):
                path.append(i)
                dfs(k, n, i + 1, path)
                path.pop()

        ans = []
        path = []
        index = 1
        dfs(k, n, index, path)
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (3, 7, [[1, 2, 4]]),
        ]
        self.s = Solution()

    def test_solution(self):
        pass


if __name__ == '__main__':
    unittest.main()
