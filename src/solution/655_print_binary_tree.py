from typing import List
from collections import deque
from src.datastruct.bin_treenode import TreeNode


class Solution:
    def get_height(self, node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def printTree(self, root: TreeNode) -> List[List[str]]:
        return self.dfs(root)

    def dfs(self, node: TreeNode) -> List[List[str]]:
        height = self.get_height(node)
        width = (1 << height) - 1
        ans = [["" for _ in range(width)] for _ in range(height)]

        def _dfs(node: TreeNode, deep: int, lo: int, hi: int):
            if node is None:
                return
            index = lo + (hi - lo) // 2
            ans[deep - 1][index] = str(node.val)
            _dfs(node.left, deep + 1, lo, index)
            _dfs(node.right, deep + 1, index + 1, hi)

        _dfs(node, 1, 0, width)
        return ans

    def bfs(self, node: TreeNode) -> List[List[str]]:
        if node is None:
            return []
        height = self.get_height(node)
        # level_size = (2 ** (height - 1) - 1) * 2 + 1
        width = (1 << height) - 1
        ans = [[" " for _ in range(width)] for _ in range(height)]

        queue = deque()
        queue.append((node, 0))
        deep = 0
        while len(queue) > 0:
            deep += 1
            level_height = (height - deep + 1)
            step = 2 ** level_height
            left_index = 2 ** (level_height - 1) - 1
            left_seq = 2 ** (deep - 1) - 1

            size = len(queue)
            for _ in range(size):
                node, seq = queue.popleft()
                cur_index = left_index + (seq - left_seq) * step
                ans[deep - 1][cur_index] = str(node.val)
                if node.left is not None:
                    queue.append((node.left, 2 * seq + 1))
                if node.right is not None:
                    queue.append((node.right, 2 * seq + 2))
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2], [["", "1", ""],
                      ["2", "", ""]]),
            ([1, 2, 3, None, 4], [["", "", "", "1", "", "", ""],
                                  ["", "2", "", "", "", "3", ""],
                                  ["", "", "4", "", "", "", ""]]),
            ([1, 2, 5, 3, None, None, None, 4], [["", "", "", "", "", "", "", "1", "", "", "", "", "", "", ""],
                                                 ["", "", "", "2", "", "", "", "", "", "", "", "5", "", "", ""],
                                                 ["", "3", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                                 ["4", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], ]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.printTree(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
