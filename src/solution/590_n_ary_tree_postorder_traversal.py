import random
from src.datastruct.n_treenode import NTreeNode as TreeNode


class Solution(object):
    def postorder(self, root):
        num = random.randint(0, 1)
        num = 0
        d = {
            0: self.dfs,
            # 1: self.preorder_traversal,
        }
        ans = d[num](root)
        return list(ans)

    def dfs(self, node):
        if node is None:
            return
        for i in node.children:
            yield from self.dfs(i)
        yield node.val


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([], []),
            (
                [1, None, 3, 2, 4, None, 5, 6],
                [5, 6, 3, 2, 4, 1],
            ),
            (
                [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None,
                 None, 14],
                [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1],
            )
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.serialize(nums)
            ans = list(self.s.postorder(root))
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
