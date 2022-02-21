from src.datastruct.treenode import TreeNode
import unittest
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        ans = 0
        queue = deque()
        queue.append([root, 0])
        while len(queue) > 0:
            size = len(queue)
            start, end = 0, 0
            for i in range(size):
                node, seq = queue.popleft()
                if i == 0:
                    start = seq
                if i == size - 1:
                    end = seq
                if node.left is not None:
                    queue.append([node.left, 2 * seq + 1])
                if node.right is not None:
                    queue.append([node.right, 2 * seq + 2])
                ans = max(ans, end - start + 1)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 3, 2, 5, 3, None, 9],4),
            ([1, 3, None, 5, 3], 2),
            ([1, 3, 2, 5], 2),
            ([1], 1),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.deserialize(nums)
            ans = self.s.widthOfBinaryTree(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
