"""
先对角线互换
再每行互换
"""
import unittest
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        clo = len(matrix[0])
        for y in range(row):
            for x in range(y, clo):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

        for m in matrix:
            m.reverse()


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
             [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])
        ]
        self.s = Solution()

    def test_solution(self):
        for matrix, answer in self.test_case:
            self.s.rotate(matrix)
            self.assertListEqual(answer, matrix)


if __name__ == '__main__':
    unittest.main()
