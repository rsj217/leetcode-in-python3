"""
`Problem <https://leetcode-cn.com/problems/>`_
-----------------------------------------------------------------------------

给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

::

    示例 1：

    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
    "ABCCED"
    输出：true

    示例 2：

    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
    "SEE"
    输出：true

    示例 3：

    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
    "ABCB"
    输出：false


    提示：

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board 和 word 仅由大小写英文字母组成

Tips
------
1. 回溯 DFS
2. 注意起点

Answer
------

"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, m, n, y, x, dct, word, idx):
            if len(word) <= idx:
                return True

            letter = word[idx]
            if letter != board[y][x]:
                return False
            nexts = []
            if 0 < y:
                top = (y - 1, x)
                nexts.append(top)
            if y < m - 1:
                bottom = (y + 1, x)
                nexts.append(bottom)
            if 0 < x:
                left = (y, x - 1)
                nexts.append(left)
            if x < n - 1:
                right = (y, x + 1)
                nexts.append(right)

            for next_ in nexts:
                next_pos = f"{next_[0]}-{next_[1]}"
                if dct.get(next_pos, False):
                    continue
                cur_pos = f"{y}-{x}"
                dct[cur_pos] = True
                ans = dfs(board, m, n, next_[0], next_[1], dct, word, idx + 1)
                if ans:
                    return True
                dct[cur_pos] = False
            return idx == len(word) - 1

        dct = {}
        idx = 0
        m = len(board)
        n = len(board[0])
        for y in range(m):
            for x in range(n):
                if board[y][x] == word[0] and dfs(board, m, n, y, x, dct, word, idx):
                    return True
        return False


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([
                 ["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]], "ABCCED", True),
            ([
                 ["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]], "SEE", True),
            ([
                 ["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]], "ABCB", False),
            ([
                 ["a"]], "a", True),
            ([
                 ["a"]], "ab", False),
            ([
                 ["a"],
                 ["a"]], "aaa", False),
            ([
                 ["a", "b", "c"],
                 ["a", "e", "d"],
                 ["a", "f", "g"]], "abcdefg", True),
        ]
        self.s = Solution()

    def test_solution(self):
        for board, word, answer in self.test_case:
            ans = self.s.exist(board, word)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
