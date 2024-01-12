import random
from typing import List
from src.datastruct.treenode import TreeNode
import unittest


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        num = random.randint(0, 2)
        num = 1
        d = {
            0: self.path_sum_by_postorder_dfs,
            1: self.path_sum_by_preorder_traversal,
            2: self.path_sum_by_postorder_traversal,
            3: self.path_sum_by_bfs,
        }
        
        return d[num](root, targetSum)
    
    def path_sum_by_preorder_traversal(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        stack = [(root, [])]
        while len(stack) > 0:
            node, path = stack.pop()
            path.append(node.val)
            
            if node.left is None and node.right is None:
                if sum(path) == targetSum:
                    ans.append(path)
                    continue
            
            if node.right is not None:
                stack.append((node.right, path.copy()))
            if node.left is not None:
                stack.append((node.left, path.copy()))
        return ans
    
    def path_sum_by_postorder_traversal(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        node = root
        stack = []
        pre_node = None
        path = []
        while True:
            while node is not None:
                path.append(node.val)
                stack.append(node)
                node = node.left
            if len(stack) <= 0:
                break
            if stack[-1].right != pre_node:
                node = stack[-1].right
                pre_node = None
            else:
                pre_node = stack.pop()
                if pre_node.left is None and pre_node.right is None and sum(path) == targetSum:
                    ans.append(path.copy())
                path.pop()
        return ans
    
    def path_sum_by_postorder_dfs(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(node: TreeNode, path_list: List[int]):
            if node is None:
                return
            
            path_list.append(node.val)
            
            if node.left is None and node.right is None:
                if sum(path_list) == targetSum:
                    ans.append(path_list)
                return
            
            dfs(node.left, path_list.copy())
            dfs(node.right, path_list.copy())
        
        dfs(root, [])
        return ans
    
    def path_sum_by_bfs(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        
        queue = [([], root)]
        while 0 < len(queue):
            path, node = queue.pop(0)
            if node.left is None and node.right is None:
                path.append(node.val)
                if sum(path) == targetSum:
                    ans.append(path)
                continue
            
            if node.left is not None:
                pleft = path.copy()
                pleft.append(node.val)
                queue.append((pleft, node.left))
            if node.right is not None:
                pright = path.copy()
                pright.append(node.val)
                queue.append((pright, node.right))
        
        return ans


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, [[5, 4, 11, 2], [5, 8, 4, 5]]),
        ]
        self.s = Solution()
    
    def test_solution(self):
        for nums, target, answer in self.test_case:
            root = TreeNode.deserialize(nums)
            ans = self.s.pathSum(root, target)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
