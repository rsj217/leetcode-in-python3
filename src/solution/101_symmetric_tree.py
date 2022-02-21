from src.datastruct.treenode import TreeNode
import unittest


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 2, 3, 4, 4, 3], True),
            ([1, 2, 2, None, 3, None, 3], False),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.deserialize(nums)
            ans = self.s.isSymmetric(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
