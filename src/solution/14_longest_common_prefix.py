"""
`Problem <https://leetcode-cn.com/problems/two-sum/>`_
--------------------------------------------------------

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。

::

    示例 1：

    输入：strs = ["flower","flow","flight"]
    输出："fl"
    示例 2：

    输入：strs = ["dog","racecar","car"]
    输出：""
    解释：输入不存在公共前缀。

    提示：

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] 仅由小写英文字母组成

Tips
------

1. 先假设第一个是ans，然后拿ans和剩下的比对，然后更新 ans
2. ans 在跟下一个比对之前，ans 要替换成 更短的那一个

Answer
------

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        assert 1 <= len(strs) <= 200
        ans = strs[0]
        for i in range(1, len(strs)):
            target = strs[i]
            if len(target) < len(ans):
                ans, target = target, ans
            for j in range(len(ans)):
                if ans[j] != target[j]:
                    ans = ans[:j]
                    break
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [
            ["flower", "flow", "flight"],
            ["dog", "racecar", "car"],
            ["", "", ""],
            ["", "qwe"],
            [""],
            ["a"],
            ["abc", "abc"],
            ["ab", "a"],
        ]
        self.answer = [
            "fl",
            "",
            "",
            "",
            "",
            "a",
            "abc",
            "a",
        ]
        self.s = Solution()

    def test_solution(self):
        for i, item in enumerate(self.input):
            ans = self.s.longestCommonPrefix(item)
            self.assertEqual(ans, self.answer[i], ans)


if __name__ == '__main__':
    unittest.main()
