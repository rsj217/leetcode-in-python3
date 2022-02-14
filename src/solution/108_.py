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
