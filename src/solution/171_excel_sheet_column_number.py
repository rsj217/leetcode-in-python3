"""
`Problem <https://leetcode-cn.com/problems/excel-sheet-column-number/>`_
-----------------------------------------------------------------------------

171. Excel 表列序号

给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

::

    示例 1:


    输入: columnTitle = "A"
    输出: 1


    示例 2:


    输入: columnTitle = "AB"
    输出: 28


    示例 3:


    输入: columnTitle = "ZY"
    输出: 701



    提示：


    1 <= columnTitle.length <= 7
    columnTitle 仅由大写英文组成
    columnTitle 在范围 ["A", "FXSHRXW"] 内



Tips
------

1. 26进制转换

Answer
------

"""

import string


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        assert 1 <= len(columnTitle) <= 7
        dct = {item: index for index, item in enumerate(string.ascii_uppercase, 1)}
        ans = 0
        for index, item in enumerate(columnTitle):
            ans += dct[item] * 26 ** (len(columnTitle) - index - 1)
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("A", 1),
            ("AB", 28),
            ("ZY", 701)
        ]
        self.s = Solution()

    def test_solution(self):
        for columnTitle, answer in self.test_case:
            ans = self.s.titleToNumber(columnTitle)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
