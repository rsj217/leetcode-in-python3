"""
`Problem <https://leetcode-cn.com/problems/trapping-rain-water/>`_
-----------------------------------------------------------------------------

42. 接雨水

给定n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


.. image:: ../../img/42.png

::

    示例 1：

    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
    示例 2：

    输入：height = [4,2,0,3,2,5]
    输出：9

    提示：

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105


Tips
------



Answer
------

"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax = height[l]
        rmax = height[r]
        ans = 0
        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if lmax <= rmax:
                ans += lmax - height[l]
                l += 1
            else:
                ans += rmax - height[r]
                r -= 1
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9),

        ]
        self.s = Solution()

    def test_solution(self):
        for height, answer in self.test_case:
            ans = self.s.trap(height)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
