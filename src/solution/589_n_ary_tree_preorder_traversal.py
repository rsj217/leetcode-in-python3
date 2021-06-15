import random
from src.datastruct.n_treenode import NTreeNode as TreeNode


class Solution(object):
    def preorder(self, root):
        num = random.randint(0, 1)
        d = {
            0: self.dfs,
            1: self.preorder_traversal,
        }
        ans = d[num](root)
        return list(ans)

    def dfs(self, node):
        if node is None:
            return
        yield node.val
        for i in node.children:
            yield from self.dfs(i)

    def preorder_traversal(self, node):
        if node is None:
            return
        stack = [node]
        while len(stack) > 0:
            node = stack.pop()
            yield node.val
            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([], []),
            (
                [1, None, 3, 2, 4, None, 5, 6],
                [1, 3, 5, 6, 2, 4]
            ),
            (
                [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None,
                 None, 14],
                [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]
            )
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = list(self.s.preorder(root))
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
