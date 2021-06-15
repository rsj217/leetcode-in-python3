import random

from src.datastruct.bin_treenode import TreeNode
import unittest


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        num = random.randint(0, 1)
        d = {
            0: self.inorder,
            1: self.dfs,
        }

        return d[num](root)

    def dfs(self, node: TreeNode) -> int:
        ans = float("inf")

        def _dfs(node: TreeNode, l: int, r: int):
            nonlocal ans
            if node is None:
                return

            if l is not None:
                ans = min(ans, node.val - l)
            if r is not None:
                ans = min(ans, r - node.val)

            _dfs(node.left, l, node.val)
            _dfs(node.right, node.val, r)

        _dfs(node, None, None)
        return ans

    def inorder(self, node: TreeNode) -> int:
        ans = float("inf")
        prev_val = -1
        stack = []
        while True:
            while node is not None:
                stack.append(node)
                node = node.left

            if len(stack) <= 0:
                break

            node = stack.pop()
            if prev_val != -1:
                ans = min(ans, node.val - prev_val)

            prev_val = node.val
            node = node.right
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([6, 3, 9, 1, 5], 1),
            ([4, 2, 6, 1, 3, None, None], 1),
            ([6, 3, None, 1], 2),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.getMinimumDifference(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
