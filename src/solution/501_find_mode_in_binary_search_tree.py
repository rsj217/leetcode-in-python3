from typing import List
from src.datastruct.treenode import TreeNode
import unittest


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        max_counts = 1
        cur_counts = 1
        prev_val = None

        for i in self.inorder(root):
            if prev_val is not None and prev_val == i:
                cur_counts += 1
            else:
                cur_counts = 1

            if max_counts == cur_counts:
                ans.append(i)
            elif max_counts < cur_counts:
                ans = [prev_val]
                max_counts = cur_counts
            prev_val = i
        return ans

    def inorder(self, node: TreeNode):
        if node is None:
            return
        yield from self.inorder(node.left)
        yield node.val
        yield from self.inorder(node.right)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, None, 2, 2], [2]),
            ([6, 5, 8, 1, 5, None, None, 1], [1, 5]),
            ([], []),
            ([1], [1]),
            ([0, None, 0], [0]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.findMode(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
