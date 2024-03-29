from src.datastruct.treenode import TreeNode
from typing import List
import random
import unittest


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        num = random.randint(0, 2)
        d = {
            0: self.dfs,
            1: self.postorder,
        }
        return list(d[num](root))

    def dfs(self, root: TreeNode):
        if root is None:
            return
        # 访问左子树
        yield from self.dfs(root.left)
        # 访问右子树
        yield from self.dfs(root.right)
        # 访问 root 节点
        yield root.val

    def postorder(self, root: TreeNode):
        pre_node = None
        node = root
        stack = []
        while True:
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) <= 0:
                break

            if stack[-1].right != pre_node:
                node = stack[-1].right
                pre_node = None
            else:
                pre_node = stack.pop()
                yield pre_node.val


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([], []),
            ([1, None, 2, 3], [3, 2, 1]),
            ([1], [1]),
            ([1, 2], [2, 1]),
            ([1, None, 2], [2, 1]),
            ([1, 2], [2, 1]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.deserialize(nums)
            ans = self.s.postorderTraversal(root)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
