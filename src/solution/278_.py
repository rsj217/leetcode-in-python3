"""
二分搜索：第一个错之后，都是错的，数组是有序的，如 [True, True, True, False, False, False]
"""
import unittest


def isBadVersion(n) -> bool:
    return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        while hi > lo:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
        ]
        self.s = Solution()

    def test_solution(self):
        pass


if __name__ == '__main__':
    unittest.main()
