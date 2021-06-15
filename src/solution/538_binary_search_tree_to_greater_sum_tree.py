from src.datastruct.bin_treenode import TreeNode
import unittest


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        return self.inorder(root)

    def inorder(self, node: TreeNode) -> TreeNode:
        stack = []
        root = node
        prev = TreeNode(val=0)
        while True:
            while node is not None:
                stack.append(node)
                node = node.right

            if len(stack) <= 0:
                break
            node = stack.pop()
            node.val += prev.val
            prev = node
            node = node.left
        return root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (
                [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
                [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
            ),

        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.convertBST(root)
            self.assertEqual(TreeNode.literal(ans), answer)


if __name__ == '__main__':
    unittest.main()
