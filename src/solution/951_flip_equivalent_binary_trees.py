from src.datastruct.treenode.treenode import TreeNode
import unittest


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node1: TreeNode, node2: TreeNode) -> bool:
            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            return (dfs(node1.left, node2.left) and dfs(node1.right, node2.right)) or (
                        dfs(node1.left, node2.right) and dfs(node1.right, node2.left))

        return dfs(root1, root2)

    # def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
    #     def dfs(node1: TreeNode, node2: TreeNode) -> bool:
    #         if node1 is None and node2 is None:
    #             return True
    #
    #         if node1 is None or node2 is None:
    #             return False
    #
    #         if node1.val != node2.val:
    #             return False
    #
    #         if node1.left is None:
    #             node1.left = node1.right
    #             node1.right = None
    #
    #         if node2.left is None:
    #             node2.left = node2.right
    #             node2.right = None
    #
    #         if node1.left is not None:
    #             if node1.right is not None:
    #                 if node2.left is not None and node2.right is not None:
    #                     if node1.left.val == node2.left.val and node1.right.val == node2.right.val:
    #                         return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
    #                     elif node1.left.val == node2.right.val and node1.right.val == node2.left.val:
    #                         return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
    #                 return False
    #             else:
    #                 if node2.left is not None and node2.right is None and node1.left.val == node2.left.val:
    #                     return dfs(node1.left, node2.left)
    #                 return False
    #         else:
    #             return node2.left is None and node2.right is None
    #
    #     return dfs(root1, root2)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 4, 5, 6, None, None, None, 7, 8], [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7], True)
        ]
        self.s = Solution()

    def test_solution(self):
        for nums1, nums2, answer in self.test_case:
            root1 = TreeNode.create(nums1)
            root2 = TreeNode.create(nums2)
            ans = self.s.flipEquiv(root1, root2)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
