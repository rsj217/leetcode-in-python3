from typing import List
import unittest


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return 0


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([3, 0, 1], 2),
            ([0, 1], 2),
            ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
            ([0], 1),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.missingNumber(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
