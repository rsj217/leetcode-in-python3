"""
`Problem <https://leetcode-cn.com/problems/merge-sorted-array/>`_
-----------------------------------------------------------------------------
88. 合并两个有序数组 ☆

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并
的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。


::

    示例 1：

    输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    输出：[1,2,2,3,5,6]
    解释：需要合并 [1,2,3] 和 [2,5,6] 。
    合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

    示例 2：

    输入：nums1 = [1], m = 1, nums2 = [], n = 0
    输出：[1]
    解释：需要合并 [1] 和 [] 。
    合并结果是 [1] 。

    示例 3：

    输入：nums1 = [0], m = 0, nums2 = [1], n = 1
    输出：[1]
    解释：需要合并的数组是 [] 和 [1] 。
    合并结果是 [1] 。
    注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。

    提示：

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10⁹ <= nums1[i], nums2[j] <= 10⁹

    进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？


Tips
------

1.插入排序算法： 将 nums2 插入到有序的 nums1 中，复杂度 Q(m*n)
2.反向归并排序，比对结果放在 nums1 末尾。

Answer
------

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
