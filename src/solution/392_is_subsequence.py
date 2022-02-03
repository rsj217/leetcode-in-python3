
"""
子序列：不连续的子串
子串：连续的子串
贪心，默认每个字符都是子串，那么两个指针，相互比对，比对成功，就匹配下一个
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0

        for si in range(len(s)):
            match = False
            for ti in range(start, len(t)):
                if s[si] == t[ti]: # 当前匹配成功
                    start = ti + 1 # 从下一个字符开始匹配下一个
                    match = True
                    break
            if not match:
                return False
        return True


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            # ("abc", "ahbgdc", True),
            # ("axc", "ahbgdc", False),
            # ("", "abc", True),
            # ("", "", True),
            # ("a", "", False),
            ("aaaaaa", "bbaaaa", False),
        ]
        self.s = Solution()

    def test_solution(self):
        for s, t, answer in self.test_case:
            ans = self.s.isSubsequence(s, t)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
