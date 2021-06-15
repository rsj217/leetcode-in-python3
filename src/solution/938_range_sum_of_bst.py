from src.datastruct.bin_treenode import TreeNode
import unittest


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self.dfs(root, low, high)

    def dfs(self, node: TreeNode, low: int, high: int) -> int:
        if node is None:
            return 0
        if low <= node.val <= high:
            return node.val + self.dfs(node.left, low, high) + self.dfs(node.right, low, high)
        elif node.val < low:
            return self.dfs(node.right, low, high)
        else:
            return self.dfs(node.left, low, high)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([10, 5, 15, 3, 7, None, 18], 7, 15, 32),
            ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, low, high, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.rangeSumBST(root, low, high)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
