from src.datastruct.treenode import TreeNode
import unittest


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode) -> (bool, int):
            if node is None:
                return True, 0
            lans, lheight = dfs(node.left)
            rans, rheight = dfs(node.right)
            curheight = 1 + max(lheight, rheight)
            if abs(lheight - rheight) <= 1 and lans and rans:
                return True, curheight
            return False, curheight
        ans, _ = dfs(root)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([], True),
            ([1], True),
            ([3, 9, 20, None, None, 15, 7], True),
            ([1, 2, None, 3], False),
            ([1, 2, 3, 4, None, None, 7, 8], False),
            ([1, 2, None, 4, None, 5], False),
            ([1, 2, None, 3, None, 4, None, 5], False),
            ([3, 2, None, 1], False),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.isBalanced(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
