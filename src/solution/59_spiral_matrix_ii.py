import unittest
from typing import List

"""
1  2  3 
8  9  4 
7  6  5

* 左闭右开
* 奇数中心点
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r = 0, n - 1
        t, b = 0, n - 1

        num = 1
        items = n * n
        ans = [[0 for _ in range(n)] for _ in range(n)]

        while num <= items:
            # left -> right
            for x in range(l, r + 1):
                ans[t][x] = num
                num += 1
            t += 1

            # top -> bottom
            for y in range(t, b + 1):
                ans[y][r] = num
                num += 1
            r -= 1

            # left <- right
            for x in range(r, l - 1, -1):
                ans[b][x] = num
                num += 1
            b -= 1

            # top <- bottom
            for y in range(b, t - 1, -1):
                ans[y][l] = num
                num += 1
            l += 1

        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (1, [[1]]),
            (2, [[1, 2], [4, 3]]),
            (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
            (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),
        ]
        self.s = Solution()

    def test_solution(self):
        for x, answer in self.test_case:
            ans = self.s.generateMatrix(x)
            self.assertListEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
