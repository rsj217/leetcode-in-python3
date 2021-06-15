from src.datastruct.bin_treenode import TreeNode
from typing import List
import unittest


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return list(self.preorder(root))

    def preorder(self, node: TreeNode):
        stack = []
        while True:
            while node is not None:
                yield node.val
                stack.append(node)
                node = node.left

            if len(stack) <= 0:
                break

            node = stack.pop()
            node = node.right

    def preorder_dfs(self, node: TreeNode):
        if node is None:
            return
        stack = [node]
        while len(stack) > 0:
            node = stack.pop()
            yield node.val
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([], []),
            ([1, None, 2, 3], [1, 2, 3]),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, None, 2], [1, 2]),
            ([1, 2, 3, 4, None, 5, 6, None, 7, None, None, 8], [1, 2, 4, 7, 3, 5, 6, 8])
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.preorderTraversal(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
