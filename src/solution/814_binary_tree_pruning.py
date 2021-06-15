from src.datastruct.bin_treenode import TreeNode
import unittest


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode) -> bool:
            if node is None:
                return True
            left = dfs(node.left)
            right = dfs(node.right)

            if left:
                node.left = None
            if right:
                node.right = None
            return left and right and node.val == 0

        return None if dfs(root) else root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([0, None, 0, 0, 0], []),
            ([1, None, 0, 0, 1], [1, None, 0, None, 1]),
            ([1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1]),
            ([1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, None, 1]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.pruneTree(root)
            self.assertEqual(answer, TreeNode.literal(ans))


if __name__ == '__main__':
    unittest.main()
