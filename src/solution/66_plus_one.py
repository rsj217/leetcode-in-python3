# https://leetcode-cn.com/problems/plus-one/
from typing import List

import unittest

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = []
        for i in range(len(digits) - 1, -1, -1):
            sum_ = digits[i] + carry
            carry = sum_ // 10
            digit = sum_ % 10
            ans.append(digit)
        if carry > 0:
            ans.append(carry)
        ans.reverse()
        return ans

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1,2,3,4], [1,2,3,5]),
            ([0], [1]),
            ([9], [1, 0]),
        ]
        self.s = Solution()

    def test_solution(self):
        for digits, answer in self.test_case:
            ans = self.s.plusOne(digits)
            self.assertListEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
