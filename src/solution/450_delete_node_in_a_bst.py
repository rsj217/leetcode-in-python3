"""
`Problem <https://leetcode-cn.com/problems/delete-node-in-a-bst/>`_
---------------------------------------------------------------------------------
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的
根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。

说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

::

    示例:

    root = [5,3,6,2,4,null,7]
    key = 3

        5
       / \\
      3   6
     / \   \\
    2   4   7

    给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

    一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

        5
       / \\
      4   6
     /     \\
    2       7

    另一个正确答案是 [5,2,6,null,4,null,7]。

        5
       / \\
      2   6
       \   \\
        4   7


Tips
------

Answer
------
"""

from src.datastruct.treenode.treenode import TreeNode


class Solution(object):
    def deleteNode(self, root, key):
        return self.delete_dfs(root, key)

    def minimum(self, node: TreeNode) -> TreeNode:
        if node.left is None:
            return node
        return self.minimum(node.left)

    def delete_dfs(self, node: TreeNode, key: int) -> TreeNode:
        if node is None:
            raise ValueError("key err")
        if key < node.val:
            node.left = self.delete_dfs(node.left, key)
        elif node.val < key:
            node.right = self.delete_dfs(node.right, key)
        else:  # node.val == val
            if node.left is None:
                rnode = node.right
                del node
                return rnode
            elif node.right is None:
                lnode = node.left
                del node
                return lnode
            else:  # node.left is not None and node.right is not None
                successor = self.minimum(node.right)
                successor.right = self.delete_dfs(node.right, successor.val)
                successor.left = node.left
                del node
                node = successor
        return node


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([4, 2, 7, 1, 3], 5, [4, 2, 7, 1, 3, 5]),
            ([40, 20, 60, 10, 30, 50, 70], 25, [40, 20, 60, 10, 30, 50, 70, None, None, 25]),
        ]
        self.s = Solution()

    def test_solution(self):
        pass  # TODO


if __name__ == '__main__':
    unittest.main()
