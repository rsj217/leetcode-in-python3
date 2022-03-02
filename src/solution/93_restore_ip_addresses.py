"""
`Problem <https://leetcode-cn.com/problems/restore-ip-addresses>`_
-----------------------------------------------------------------------------

93. 复原IP地址

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
和 "192.168@1.1" 是 无效 IP 地址。

给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新
排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

::

    示例 1：

    输入：s = "25525511135"
    输出：["255.255.11.135","255.255.111.35"]

    示例 2：

    输入：s = "0000"
    输出：["0.0.0.0"]

    示例 3：

    输入：s = "101023"
    输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

    提示：


    1 <= s.length <= 20
    s 仅由数字组成

Tips
------

1.回溯

Answer
--------

"""

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(s, size, index, path, ans):
            if len(path) == 4:
                if index == size:
                    ans.append(".".join(path[:]))
                return
            for i in range(index, index + 3):
                if i + 1 > size:
                    return
                n = s[index:i + 1]
                if len(n) > 1 and n.startswith("0"):
                    return
                if int(n) > 255:
                    return
                path.append(n)
                dfs(s, size, i + 1, path, ans)
                path.pop()

        size = len(s)
        ans = []
        dfs(s, size, 0, [], ans)
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("25525511135", ["255.255.11.135", "255.255.111.35"]),
            ("0000", ["0.0.0.0"]),
            ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
        ]
        self.s = Solution()

    def test_solution(self):
        for s, answer in self.test_case:
            ans = self.s.restoreIpAddresses(s)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
