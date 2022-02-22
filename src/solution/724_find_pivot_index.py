"""
`Problem <https://leetcode-cn.com/problems/find-pivot-index/>`_
-----------------------------------------------------------------------------
724. 寻找数组的中心下标

给你一个整数数组 nums ，请计算数组的 中心下标 。

数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。

::

    示例 1：

    输入：nums = [1, 7, 3, 6, 5, 6]
    输出：3
    解释：
    中心下标是 3 。
    左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
    右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。

    示例 2：

    输入：nums = [1, 2, 3]
    输出：-1
    解释：
    数组中不存在满足此条件的中心下标。

    示例 3：

    输入：nums = [2, 1, -1]
    输出：0
    解释：
    中心下标是 0 。
    左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
    右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。

    提示：

    1 <= nums.length <= 10⁴
    -1000 <= nums[i] <= 1000



Tips
------

对于中心索引  i， 符合条件的是 sum(0 ~ i-1)  和  sum(i+1, len-1)

sum[i] = sum[i-1] + nums[i]

动态规划，提前计算 前 i 和 后 i 个的和

Answer
------

"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # left 下标 i 表示 前 i 的和
        left = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            left[i+1] = left[i] + nums[i]
        # right 下标 i 表示 后 i 的和
        right = [0] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            right[len(nums) - i] = right[len(nums) - i - 1] + nums[i]

        for i in range(len(nums)):
            # i 的左边 前 i 个 和 i 的右边，后 i 个
            if left[i] == right[len(nums) - 1 - i]:
                return i
        return -1

    def vio_search(self, nums):
        for i in range(len(nums)):
            lsum = 0
            for l in range(0, i):
                lsum += nums[l]
            rsum = 0
            for r in range(i + 1, len(nums)):
                rsum += nums[r]
            if lsum == rsum:
                return i
        return -1


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 7, 3, 6, 5, 6], 3),
            ([1, 2, 3], -1),
            ([2, 1, -1], 0),
            ([0], 0),
            ([1], 0),
            ([1, 0], 0),
            ([0, 1], 1),

        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.pivotIndex(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
