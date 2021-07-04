"""
`Problem <https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/>`_
--------------------------------------------------------------------------------------

给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于
node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：


节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。


> 注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/ 相同

::

    示例 1：

    输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

    示例 2：

    输入：root = [0,null,1]
    输出：[1,null,1]

    示例 3：

    输入：root = [1,0,2]
    输出：[3,3,2]

    示例 4：

    输入：root = [3,2,4,1]
    输出：[7,9,4,10]

Tips
------



Answer
------

"""

from src.datastruct.bin_treenode import TreeNode
import unittest
import random


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        num = random.randint(0, 1)
        d = {
            0: self.inorder,
            1: self.dfs,
        }
        return d.get(num)(root)

    def dfs(self, root: TreeNode) -> TreeNode:
        def dfs_(node: TreeNode, sum_: int) -> int:
            if node is None:
                return sum_
            sum_ = dfs_(node.right, sum_)
            sum_ += node.val
            node.val = sum_
            return dfs_(node.left, sum_)

        dfs_(root, 0)
        return root

    def inorder(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        node = root
        sum_ = 0
        stack = []
        while True:
            while node is not None:
                stack.append(node)
                node = node.right
            if len(stack) <= 0:
                break

            node = stack.pop()
            sum_ += node.val
            node.val = sum_
            node = node.left
        return root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
             [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]),
            ([0, None, 1], [1, None, 1]),
            ([1, 0, 2], [3, 3, 2]),
            ([3, 2, 4, 1], [7, 9, 4, 10]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.bstToGst(root)
            self.assertEqual(answer, TreeNode.literal(ans))


if __name__ == '__main__':
    unittest.main()
