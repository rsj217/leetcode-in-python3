"""
`Problem <https://leetcode-cn.com/problems/maximum-binary-tree/>`_
-------------------------------------------------------------------

给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：

二叉树的根是数组 nums 中的最大元素。
左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。

返回有给定数组 nums 构建的 最大二叉树 。

::

    示例 1：

    输入：nums = [3,2,1,6,0,5]
    输出：[6,3,5,null,2,0,null,null,1]
    解释：递归调用如下所示：
    - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
    - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
        - 空数组，无子节点。
        - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
            - 空数组，无子节点。
            - 只有一个元素，所以子节点是一个值为 1 的节点。
    - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
        - 只有一个元素，所以子节点是一个值为 0 的节点。
        - 空数组，无子节点。


    示例 2：

    输入：nums = [3,2,1]
    输出：[3,null,2,null,1]


    提示：

    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000
    nums 中的所有整数 互不相同

Tips
------


Answer
------

"""

from typing import List
from src.datastruct.treenode import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def dfs(nums: List[int]) -> TreeNode:
            if len(nums) <= 0:
                return None
            max_item = max(nums)
            mid = nums.index(max_item)
            root = TreeNode(max_item)

            root.left = dfs(nums[0:mid])
            root.right = dfs(nums[mid + 1:len(nums)])
            return root

        return dfs(nums)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([3, 2, 1, 6, 0, 5], [6, 3, 5, None, 2, 0, None, None, 1]),
            ([3, 2, 1], [3, None, 2, None, 1])
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.constructMaximumBinaryTree(nums)
            self.assertEqual(answer, TreeNode.literal(ans))


if __name__ == '__main__':
    unittest.main()
