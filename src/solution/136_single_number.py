from typing import List


"""
异或运算
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([4,1,2,1,2], 4),
            ([2,2,1], 1)
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.singleNumber(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
