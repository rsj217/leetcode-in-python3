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
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(x, y, d, idx):
            if len(word) <= idx:  # 单词搜索完毕，没有发现不匹配的，返回 True
                return True
            else:
                # 坐标越界
                if col <= x or x < 0 or row <= y or y < 0:
                    return False
            
            # 已搜索过路径
            if d.get(f"{y}-{x}", False):
                return False
            # 当前单词判等
            if board[y][x] != word[idx]:
                return False
            else:
                # 更新搜索状态
                d[f"{y}-{x}"] = True
                
                # 搜索上下左右
                for m, n in dirs:
                    if dfs(x+m,y+n, d, idx+1):
                        return True
                # 恢复状态
                d[f"{y}-{x}"] = False
            # 没有搜索结果
            return False
        
        d = dict()
        idx = 0
        row = len(board)
        col = len(board[0])
        
        for y in range(row):
            for x in range(col):
                if dfs(x, y, d, idx):
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
            
            ([
                 ["A", "A", "A", "A", "A", "A"],
                 ["A", "A", "A", "A", "A", "A"],
                 ["A", "A", "A", "A", "A", "A"],
                 ["A", "A", "A", "A", "A", "A"],
                 ["A", "A", "A", "A", "A", "A"],
                 ["A", "A", "A", "A", "A", "A"]], "AAAAAAAAAAAAAAa", False)
        ]
        self.s = Solution()
    
    def test_solution(self):
        for board, word, answer in self.test_case:
            ans = self.s.exist(board, word)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
