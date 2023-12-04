from src.datastruct.treenode import TreeNode
import unittest


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        path_max = float("-inf")
        ans = 0
        stack = [root]
        while 0 < len(stack):
            node = stack.pop()
            if path_max <= node.val:
                ans += 1
                path_max = max(path_max, node.val)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([-4, -4, 5, None, None, 4, -5, -5, 2, 1, None, None, -2, None, 5, None, None, None, -4, None, None, -4,
               None, 2, None, -1], 4),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.deserialize(nums)
            ans = self.s.goodNodes(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
