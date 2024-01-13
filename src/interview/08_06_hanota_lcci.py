from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        
        def hanota_(n, A, B, C):
            if n == 1:
                C.append(A.pop())
                return
            hanota_(n - 1, A, C, B)
            hanota_(1, A, B, C)
            hanota_(n - 1, B, A, C)
        
        hanota_(len(A), A, B, C)


import unittest


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            ([2, 1, 0], [], [], [2, 1, 0])
        ]
        self.s = Solution()
    
    def test_solution(self):
        for A, B, C, answer in self.test_case:
            self.s.hanota(A, B, C)
            self.assertEqual(C, answer)


if __name__ == '__main__':
    unittest.main()
