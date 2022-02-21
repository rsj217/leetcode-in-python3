"""
`Problem <https:leetcode-cn.com/problems/validate-binary-search-tree/>`_
-------------------------------------------------------------------------

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

* 节点的左子树只包含小于当前节点的数。
* 节点的右子树只包含大于当前节点的数。
* 所有左子树和右子树自身必须也是二叉搜索树。

::

    示例 1:
    输入:
      2
     / \\
    1   3
    输出: true

    示例 2:
    输入:
      5
     / \\
    1   4
       / \\
      3   6
    输出: false
    解释: 输入为: [5,1,4,null,null,3,6]。
        根节点的值为 5 ，但是其右子节点值为 4 。

Tips
------

方法一 中序遍历:

使用中序遍历的顺序是树节点的投影性质。存储一个 ``prev`` 节点，每次访问节点的时候比较 ``prev < curnode`` 。
如果不是单调递增，则不符合二叉搜索树的定义。即可返回结果

方法二 DFS递归：

根据二叉树搜索树的定义，``左边的节点 < 当前节点 < 右边的节点`` 左边的节点可能是左孩子，也可能是左孩子的右孩子

::

     10
    /
  5
   \\
    8

因此每次递归的时候，需要传入一个下界（左边最大值）和一个上界（右边最小值）。使用 DFS 递归遍历即可。伪代码如下：

::

    def dfs(node, lval, rval) -> bool:
        # 空树属于二叉搜索树
        if node is None:
            return True

        # 当前节点在 (lval, rval) 区间内，递归左右子树
        if lval < node.val < rval:
            # 递归左子树，当前节点为左子树的上界。
            lvalid =  dfs(node.left, lval, node.val)
            # 递归右子树，当前节点为右子树的下界。
            rvalid =  dfs(node.right, node.val, rval)
            # 左右子树都是二叉搜索树
            return lvalid and rvalid
        else: # 当前节点不在 (lval, rval) 区间内，不符合二叉搜索树定义，返回 False
            return False

dfs 方法中，通常可以使用 ``and`` 或 ``or`` 逻辑表达式通过短路提前返回，优化性能 ``return dfs(node.left) and dfs(node.right)``

Answer
------

"""
import random

from src.datastruct.treenode import TreeNode
import unittest


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        num = random.randint(0, 1)
        data = {
            0: self.inorder,
            1: self.dfs,
        }
        return data[num](root)

    def inorder(self, node: TreeNode) -> bool:
        """ 中序遍历 """
        prev = TreeNode(val=float("-inf"))
        stack = []
        while True:
            while node is not None:
                stack.append(node)
                node = node.left
            if not stack:
                break
            node = stack.pop()
            if node.val <= prev.val:
                return False
            prev = node
            node = node.right
        return True

    def dfs(self, node: TreeNode) -> bool:
        """ dfs 递归遍历 """
        def _dfs(node: TreeNode, lval, rval) -> bool:
            if node is None:
                return True
            if lval < node.val < rval:
                return _dfs(node.left, lval, node.val) and _dfs(node.right, node.val, rval)
            else:
                return False

        return _dfs(node, float("-inf"), float("inf"))


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([2, 1, 3], True),
            ([1, 1], False),
            ([5, 1, 4, None, None, 3, 6], False),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.deserialize(nums)
            ans = self.s.isValidBST(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
