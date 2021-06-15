"""
`Problem <https://leetcode-cn.com/problems/combinations/>`_
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



Answer
------

"""

import unittest
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(index, path):
            if len(path) == k:
                ans.append(path[:])
                return ans
            for i in range(index, n+1):
                path.append(i)
                backtracking(i+1, path)
                path.pop()
        ans = []
        backtracking(1, [])
        return ans




class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (1, 1, [[1]]),
            (4, 2, [
                [1, 2],
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
                [3, 4],
            ]),
        ]
        self.s = Solution()

    def test_solution(self):
        for n, k, answer in self.test_case:
            ans = self.s.combine(n, k)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
