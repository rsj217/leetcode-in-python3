"""
`Problem <https://leetcode-cn.com/problems/zigzag-conversion/>`_
-----------------------------------------------------------------------------

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

::

    P   A   H   N
    A P L S I I G
    Y   I   R

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

::

    示例 1：

    输入：s = "PAYPALISHIRING", numRows = 3
    输出："PAHNAPLSIIGYIR"

    示例 2：

    输入：s = "PAYPALISHIRING", numRows = 4
    输出："PINALSIGYAHRPI"
    解释：

    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    示例 3：

    输入：s = "A", numRows = 1
    输出："A"

    提示：

    1 <= s.length <= 1000
    s 由英文字母（小写和大写）、',' 和 '.' 组成
    1 <= numRows <= 1000


Tips
------
模拟
1. 二维矩阵, 一共 numRow 行
2. 从上往下打印, 对应的行添加字符
3. 再从下往上打印

Answer
------

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        assert 1 <= len(s) <= 1000
        assert 1 <= numRows <= 1000
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows)]
        row = 0
        up2bottom = False
        for item in s:
            ans[row].append(item)
            if row == numRows - 1 or row == 0:
                up2bottom = not up2bottom
            if up2bottom:
                row += 1
            else:
                row -= 1
        return "".join(["".join(item) for item in ans])


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("A", 1, "A"),
            ("A", 2, "A"),
            ("ABC", 1, "ABC"),
            ("ABC", 2, "ACB"),
            ("ABC", 3, "ABC"),

        ]
        self.s = Solution()

    def test_solution(self):
        for s, numRows, answer in self.test_case:
            ans = self.s.convert(s, numRows)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
