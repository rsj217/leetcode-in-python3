"""
`Problem <https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/>`_
--------------------------------------------------------------------------------------------
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。


::

    示例 1：


    输入：nums = [-10,-3,0,5,9]
    输出：[0,-3,9,-10,null,5]
    解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：



    示例 2：


    输入：nums = [1,3]
    输出：[3,1]
    解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。

    提示：

    1 <= nums.length <= 10⁴
    -10⁴ <= nums[i] <= 10⁴
    nums 按 严格递增 顺序排列

Tips
------


Answer
------
"""

from typing import List
from src.datastruct.treenode import TreeNode, print_tree
import unittest


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(nums, lo, hi):
            if hi - lo <= 0:
                return None
            if hi - lo == 1:
                return TreeNode(val=nums[lo])
            mid = lo + (hi - lo) // 2
            node = TreeNode(val=nums[mid])
            node.left = dfs(nums, lo, mid)
            node.right = dfs(nums, mid + 1, hi)
            return node

        return dfs(nums, 0, len(nums))


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
        ]
        self.s = Solution()

    def test_solution(self):
        pass


if __name__ == '__main__':
    unittest.main()
