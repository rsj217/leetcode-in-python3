from typing import List
import unittest


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([1], [1]),
            ([0], [0]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            self.s.moveZeroes(nums)
            self.assertListEqual(nums, answer)


if __name__ == '__main__':
    unittest.main()
