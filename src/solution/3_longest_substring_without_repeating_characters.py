"""
`Problem <https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/>`_
--------------------------------------------------------
3. 无重复字符的最长子串

给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

::

    示例1:

    输入: s = "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    示例 2:

    输入: s = "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    示例 3:

    输入: s = "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

    提示：

    0 <= s.length <= 5 * 104
    s 由英文字母、数字、符号和空格组成

Tips
------
1，滑动窗口
2. 窗口的定义，字符的计数
Answer
------

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo, hi = 0, 0
        ans = 0
        window = dict()
        while hi < len(s):
            window[s[hi]] = window.get(s[hi], 0) + 1
            hi += 1

            while window[s[hi - 1]] > 1:
                window[s[lo]] -= 1
                lo += 1
            ans = max(ans, hi - lo)
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("abcabcbb", 3),
            ("bbbb", 1),
            ("pwwkew", 3),
        ]
        self.s = Solution()

    def test_solution(self):
        for s, answer in self.test_case:
            ans = self.s.lengthOfLongestSubstring(s)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
