"""
`Problem <https://leetcode-cn.com/problems/one-edit-distance>`_
-----------------------------------------------------------------------------

161. 相隔为1的编辑距离

给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。

注意：

满足编辑距离等于 1 有三种可能的情形：


* 往 s 中插入一个字符得到 t
* 从 s 中删除一个字符得到 t
* 在 s 中替换一个字符得到 t

::

    示例 1：

    输入: s = "ab", t = "acb"
    输出: true
    解释: 可以将 'c' 插入字符串 s来得到 t。

    示例 2:

    输入: s = "cab", t = "ad"
    输出: false
    解释: 无法通过 1 步操作使 s 变为 t。

    示例 3:

    输入: s = "1203", t = "1213"
    输出: true
    解释: 可以将字符串 s中的 '0' 替换为 '1' 来得到 t。

Tips
------

1. 双指针，两个字符比对对应的位置
2. 长度大于1的排除，剩余两种情况，长度相等，长度小于1。最短的插入一个变最长，最长删减一个变最短。两种算法一样
3. 使用短的和长的字串按照位置比对

Answer
------

"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        d = len(s) - len(t)
        if d == 0:
            ans = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    ans += 1
            return ans == 1
        elif d == -1 or d == 1:
            ss, tt = (s, t) if len(s) < len(t) else (t, s)
            i, j = 0, 0
            ans = 0
            while i < len(ss) and j < len(tt):
                if ss[i] != tt[j]:
                    j += 1
                    ans += 1
                    continue
                i += 1
                j += 1
            return ans <= 1
        else:
            return False


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("ab", "ab", False),
            ("ab", "ac", True),
            ("ab", "acb", True),
            ("", "a", True),
            ("", "", False),
            ("ab", "abc", True),
            ("tache", "teacher", False),
        ]
        self.s = Solution()

    def test_solution(self):
        for s, t, answer in self.test_case:
            ans = self.s.isOneEditDistance(s, t)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
