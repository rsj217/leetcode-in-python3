"""
`Problem <https://leetcode-cn.com/problems/isomorphic-strings/>`_
-----------------------------------------------------------------------------

205. 同构字符串

给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

::

    示例 1:

    输入：s = "egg", t = "add"
    输出：true

    示例 2：

    输入：s = "foo", t = "bar"
    输出：false

    示例 3：

    输入：s = "paper", t = "title"
    输出：true

    提示：

    1 <= s.length <= 5 * 10⁴
    t.length == s.length
    s 和 t 由任意有效的 ASCII 字符组成

Tips
------

1. hash 记录字符映射表
2. 记录已映射的字符

Answer
------

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        assert len(s) == len(t)
        dct = dict()
        used = []
        for i in range(len(s)):
            if s[i] not in dct:
                if t[i] in used:
                    # 同一字符映射多个字符
                    return False
                dct[s[i]] = t[i]
                used.append(t[i])
            else:
                if dct[s[i]] != t[i]:
                    return False
        return True


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("egg","add",True),
            ("foo","bar", False),
            ("paper","title", True),
            ("bbbaaaba", "aaabbbba", False),
            ("badc", "babc", False),
        ]
        self.s = Solution()

    def test_solution(self):
        for s, t, answer in self.test_case:
            ans = self.s.isIsomorphic(s, t)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
