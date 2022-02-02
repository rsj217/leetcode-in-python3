from typing import List
import unittest

# slide window

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 0
        sum_ = 0
        lo, hi = 0, 0
        while hi < len(nums):
            sum_ += nums[hi]
            hi += 1
            while target <= sum_:
                if ans > 0:
                    ans = min(ans, hi - lo)
                else:
                    ans = hi - lo
                sum_ -= nums[lo]
                lo += 1
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (7, [2, 3, 1, 2, 4, 3], 2),
            (4, [1, 4, 4], 1),
            (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        ]
        self.s = Solution()

    def test_solution(self):
        for target, nums, answer in self.test_case:
            ans = self.s.minSubArrayLen(target, nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
