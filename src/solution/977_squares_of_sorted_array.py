from typing import List
import unittest

# 归并排序思想，合并两个有序数组

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        ans = []
        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                ans.append(nums[j] ** 2)
                j -= 1
            else:
                ans.append(nums[i] ** 2)
                i += 1
        ans.reverse()
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([-4, -1, 0, 3, 10]),
            ([-7, -3, 2, 3, 11]),
            ([-5, -3, -2, -1]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums in self.test_case:
            ans = self.s.sortedSquares(nums)
            answer = [i ** 2 for i in nums]
            answer.sort()
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
