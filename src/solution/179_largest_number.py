"""
`Problem <https://leetcode-cn.com/problems/largest-number/>`_
-----------------------------------------------------------------------------

179. 最大数

给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

::

    示例 1：

    输入：nums = [10,2]
    输出："210"

    示例 2：

    输入：nums = [3,30,34,5,9]
    输出："9534330"

    提示：
    0 <= nums[i] <= 10⁹


Tips
------

1. 字符串拼接比较， 例如 a=3 b=30， ab = 330 ， ba=303，比较 ab 和 ab 进行排序
2. 对于 0 开头的是非法数字，需要排除

Answer
------

"""

import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_list = [str(i) for i in nums]
        
        def compare(a, b):
            ab = a + b
            ba = b + a
            return 1 if ab < ba else -1
        
        nums_list.sort(key=functools.cmp_to_key(compare))
        return "0" if nums_list[0] == "0" else "".join(nums_list)


import unittest


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            ([10, 2, 9, 39, 17], "93921710"),
            ([3, 30, 34, 5, 9], "9534330"),
            ([10, 2], "210"),
            ([0, 1], "10"),
            ([0, 0], "0"),
        ]
        self.s = Solution()
    
    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.largestNumber(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
