from src.datastruct.treenode import TreeNode
from typing import Optional
import unittest


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        def dfs(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
            if root is None:
                return
            if root.val == p.val or root.val == q.val:
                return root
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            
            if left is not None and right is not None:
                return root
            elif left is not None:
                return left
            elif right is not None:
                return right
            else:
                return None
        
        return dfs(root, p, q)


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
            ([1, 2], 1, 2, 1),
        ]
        self.s = Solution()
    
    def test_solution(self):
        for nums, p, q, answer in self.test_case:
            root = TreeNode.deserialize(nums)
            p = TreeNode(p)
            q = TreeNode(q)
            ans = self.s.lowestCommonAncestor(root, p, q)
            self.assertEqual(answer, ans.val)


if __name__ == '__main__':
    unittest.main()
