"""
`Problem <https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/>`_
-------------------------------------------------------------------------------------

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

::

    示例 1：

    输入：digits = "23"
    输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
    示例 2：

    输入：digits = ""
    输出：[]
    示例 3：

    输入：digits = "2"
    输出：["a","b","c"]
     

    提示：

    0 <= digits.length <= 4
    digits[i] 是范围 ['2', '9'] 的一个数字。


Tips
------


Answer
--------
"""
import random
from typing import List
import unittest


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        num = random.randint(0, 1)
        d = {
            0: self.dfs,
            1: self.backtracking,
        }
        return d[num](digits)

    def dfs(self, digits: str) -> List[str]:
        if len(digits) <= 0:
            return []

        digit_letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def _dfs(digits: str, index: int, path: str):
            if index == len(digits):
                ans.append(path)
                return

            letters = digit_letter_map[digits[index]]
            for letter in letters:
                _dfs(digits, index + 1, path + letter)

        ans = []
        _dfs(digits, 0, "")
        return ans

    def backtracking(self, digits: str) -> List[str]:
        if len(digits) <= 0:
            return []

        digit_letter_map = {
            '0': ' ',
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def _backtracking(track: List[str], index: int):
            if index == len(digits):
                ans.append("".join(track))
                return

            letters = digit_letter_map[digits[index]]
            for letter in letters:
                track.append(letter)
                _backtracking(track, index + 1)
                track.pop()

        ans = []
        _backtracking([], 0)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("", []),
            ("23", [
                "ad", "ae", "af",
                "bd", "be", "bf",
                "cd", "ce", "cf"]),
            ("234", [
                "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
                "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
                "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]),
            ("222", [
                "aaa", "aab", "aac", "aba", "abb", "abc", "aca", "acb", "acc",
                "baa", "bab", "bac", "bba", "bbb", "bbc", "bca", "bcb", "bcc",
                "caa", "cab", "cac", "cba", "cbb", "cbc", "cca", "ccb", "ccc"]),
            ("999",
             ["www", "wwx", "wwy", "wwz", "wxw", "wxx", "wxy", "wxz", "wyw", "wyx", "wyy", "wyz", "wzw", "wzx", "wzy",
              "wzz",
              "xww", "xwx", "xwy", "xwz", "xxw", "xxx", "xxy", "xxz", "xyw", "xyx", "xyy", "xyz", "xzw", "xzx", "xzy",
              "xzz",
              "yww", "ywx", "ywy", "ywz", "yxw", "yxx", "yxy", "yxz", "yyw", "yyx", "yyy", "yyz", "yzw", "yzx", "yzy",
              "yzz",
              "zww", "zwx", "zwy", "zwz", "zxw", "zxx", "zxy", "zxz", "zyw", "zyx", "zyy", "zyz", "zzw", "zzx", "zzy",
              "zzz"]),
        ]
        self.s = Solution()

    def test_solution(self):
        for digits, answer in self.test_case:
            ans = self.s.letterCombinations(digits)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
