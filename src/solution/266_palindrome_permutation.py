"""
`Problem <https://leetcode-cn.com/problems/palindrome-permutation/>`_
-----------------------------------------------------------------------------
266. 回文排列

给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。

::

    示例 1：

    输入: "code"
    输出: false
    示例 2：

    输入: "aab"
    输出: true
    示例 3：

    输入: "carerac"
    输出: true


::

    示例 1：

    入：nums = [2,7,11,15], target = 9
    出：[0,1]
    释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。



    提示：

    2 <= nums.length <= 103


Tips
------

1. 哈希存储字符个数
2. 偶数相消后没有多余的数，或只剩一个数

时间：O(n)
空间：O(n)

Answer
------

"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dct = {}
        for item in s:
            if dct.get(item, 0) == 0:
                dct[item] = 1
            else:
                dct[item] = dct[item] - 1

        num = 0
        for _, v in dct.items():
            if v >= 1:
                num += 1
        return num <= 1


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("code", False),
            ("aab", True),
            ("carerac", True),
        ]
        self.s = Solution()

    def test_solution(self):
        for s, answer in self.test_case:
            ans = self.s.canPermutePalindrome(s)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
