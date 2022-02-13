"""
`Problem <https://leetcode-cn.com/problems/reverse-string//>`_
-------------------------------------------------------------

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。


::

    示例 1：

    输入：s = ["h","e","l","l","o"]
    输出：["o","l","l","e","h"]
    示例 2：

    输入：s = ["H","a","n","n","a","h"]
    输出：["h","a","n","n","a","H"]

    提示：

    1 <= s.length <= 105
    s[i] 都是 ASCII 码表中的可打印字符

Tips
------

Answer
------

"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (2, 1),
            (3, 2),
            (4, 4),
            (5, 6),
            (6, 9),
            (7, 12),
            (8, 18),
            (9, 27),
        ]
        self.s = Solution()

    def test_solution(self):
        for n, answer in self.test_case:
            ans = self.s.integerBreak(n)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
