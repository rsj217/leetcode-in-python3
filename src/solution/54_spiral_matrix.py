import unittest
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, n - 1
        t, b = 0, m - 1
        num = m * n

        ans = []

        while 0 < num:
            print(num)
            # l -> r
            for x in range(l, r + 1):
                ans.append(matrix[t][x])
                num -= 1
            t += 1

            print(num)

            # t -> b
            for y in range(t, b + 1):
                ans.append(matrix[y][r])
                num -= 1
            r -= 1

            # l <- r
            for x in range(r, l - 1, -1):
                ans.append(matrix[b][x])
                num -= 1
            b -= 1

            # t <- b
            for y in range(b, t - 1, -1):
                ans.append(matrix[y][l])
                num -= 1
            l += 1

        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            # ([[1]], [1]),
            # ([[1, 2], [3, 4]], [1, 2, 4, 3]),
            # ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ]
        self.s = Solution()

    def test_solution(self):
        for matrix, answer in self.test_case:
            ans = self.s.spiralOrder(matrix)
            self.assertListEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
