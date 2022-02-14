"""
1.插入排序算法： 将 nums2 插入到有序的 nums1 中，复杂度 Q(m*n)
2.反向归并排序，比对结果放在 nums1 末尾。

"""

from typing import List
import unittest


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # self.insert_sort(nums1, m, nums2, n)
        self.merge_sort(nums1, m, nums2, n)

    def merge_sort(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r = m + n - 1
        i = m - 1
        j = n - 1

        while 0 <= i and 0 <= j:
            if nums1[i] < nums2[j]:
                nums1[r] = nums2[j]
                j -= 1
            else:
                nums1[i], nums1[r] = nums1[r], nums1[i]
                i -= 1
            r -= 1
        while 0 <= j:
            nums1[r] = nums2[j]
            j -= 1
            r -= 1

    def insert_sort(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            x = nums2[i]
            j = m + i
            while 0 < j and x < nums1[j - 1]:
                nums1[j] = nums1[j - 1]
                j -= 1
            nums1[j] = x


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            ([1], 1, [], 0, [1])
        ]
        self.s = Solution()

    def test_solution(self):
        for nums1, m, nums2, n, answer in self.test_case:
            self.s.merge(nums1, m, nums2, n)
            self.assertListEqual(answer, nums1)


if __name__ == '__main__':
    unittest.main()
