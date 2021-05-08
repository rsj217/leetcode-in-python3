from typing import List
from collections import deque
import unittest
import random


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        cur = self.val
        left = self.left.val if self.left is not None else ""
        right = self.right.val if self.right is not None else ""
        return f"{left}<-{cur}->{right}"

    def __repr__(self):
        return self.__str__()

    @property
    def height(self):
        return self._get_height(self)

    def _get_height(self, node) -> int:
        if not node:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    @classmethod
    def create(cls, nums: List[int]):
        nums_size = len(nums)
        if nums_size <= 0:
            return None

        root = cls(nums[0])
        queue = deque()
        queue.append(root)
        # 数组index
        index = 0
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                lseq = 2 * index + 1
                rseq = 2 * index + 2
                if lseq < nums_size and nums[lseq] is not None:
                    node.left = cls(nums[lseq])
                    queue.append(node.left)
                if rseq < nums_size and nums[rseq] is not None:
                    node.right = cls(nums[rseq])
                    queue.append(node.right)
                index += 1
        return root


def print_tree(node) -> str:
    num = random.randint(0, 1)
    num = 1
    d = {
        0: print_tree_dfs,
        1: print_tree_bfs,
    }
    ans = d[num](node)
    return "\n".join(["".join(line) for line in ans])


def print_tree_bfs(node: TreeNode) -> List[List[str]]:
    if node is None:
        return []
    height = node.height
    width = (1 << height) - 1
    levels = [[" " for _ in range(width)] for _ in range(height)]

    queue = deque()
    queue.append((node, 0))
    deep = 0
    while len(queue) > 0:
        deep += 1
        level_height = (height - deep + 1)
        step = 2 ** level_height
        left_index = 2 ** (level_height - 1) - 1
        left_seq = 2 ** (deep - 1) - 1

        size = len(queue)
        for _ in range(size):
            node, seq = queue.popleft()
            cur_index = left_index + (seq - left_seq) * step
            levels[deep - 1][cur_index] = str(node.val)
            if node.left is not None:
                queue.append((node.left, 2 * seq + 1))
            if node.right is not None:
                queue.append((node.right, 2 * seq + 2))
    return levels


def print_tree_dfs(node: TreeNode) -> List[List[str]]:
    height = node.height
    width = (1 << height) - 1
    ans = [[" " for _ in range(width)] for _ in range(height)]

    def dfs(node: TreeNode, deep: int, lo: int, hi: int):
        if node is None:
            return
        mid = lo + (hi - lo) // 2
        ans[deep - 1][mid] = str(node.val)
        dfs(node.left, deep + 1, lo, mid)
        dfs(node.right, deep + 1, mid + 1, hi)

    dfs(node, 1, 0, width)
    return ans


def tree_deep(node: TreeNode) -> int:
    max_deep = 0

    def dfs(node: TreeNode, level: int):
        nonlocal max_deep
        if node is None:
            return
        max_deep = max(max_deep, level)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(node, 0)
    return max_deep


def tree_literal(node: TreeNode) -> List[int]:
    if node is None:
        return []
    max_deep = tree_deep(node)
    ret = [node.val]
    queue = [node]

    deep = -1
    while len(queue) > 0:
        size = len(queue)
        deep += 1
        for i in range(size):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if deep < max_deep:
                left, right = None, None
                if node.left is not None:
                    left = node.left.val
                if node.right is not None:
                    right = node.right.val
                ret.append(left)
                ret.append(right)

    for i in range(len(ret) - 1, -1, -1):
        if ret[i] is None:
            ret.pop()
        else:
            break
    return ret


class TestTreeNode(unittest.TestCase):

    def test_create(self):
        nums = []
        root = TreeNode.create(nums)
        self.assertIsNone(root)

        nums = [1, 2, 3]
        root = TreeNode.create(nums)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)

        self.assertEqual(nums, tree_literal(root))

        nums = [1, None, 2, 3]
        root = TreeNode.create(nums)
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.left.val, 3)

        self.assertEqual(nums, tree_literal(root))

        nums = [1, 2, 3, None, 4, 5]
        root = TreeNode.create(nums)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertIsNone(root.left.left)
        self.assertEqual(root.left.right.val, 4)
        self.assertEqual(root.right.left.val, 5)

        self.assertEqual(nums, tree_literal(root))

        nums = [1, 2, 3, None, None, 5]
        root = TreeNode.create(nums)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.right.left.val, 5)

        self.assertEqual(nums, tree_literal(root))

        nums = [1, 2, 3, None, None, 5, None, 6]
        root = TreeNode.create(nums)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.right.left.val, 5)
        self.assertIsNone(root.right.right)
        self.assertEqual(root.right.left.left.val, 6)

        self.assertEqual(nums, tree_literal(root))


class TestPrintTreeNode(unittest.TestCase):

    def test_empty(self):
        root = TreeNode.create([])
        print(print_tree(root))

    def test_print_tree(self):
        # root = TreeNode.create([1, 2, None, 2, None, 3])
        # root = TreeNode.create([1, 2, 3, 4, None, 5, 6, None, 7, None, None, 8])
        # print(print_tree(root))
        #
        # nums = [1, None, 2, 3]
        # root = TreeNode.create(nums)
        # print(print_tree(root))
        #
        # nums = [1, 2, None, 3]
        # root = TreeNode.create(nums)
        # print(print_tree(root))

        nums = [1, 2, 3, None, 4, 5]
        root = TreeNode.create(nums)
        print(print_tree(root))
        #
        # nums = [1, 2, 3, None, None, 5]
        # root = TreeNode.create(nums)
        # print(print_tree(root))
        #
        # nums = [1, 2, 3, None, None, 5, None, 6]
        # root = TreeNode.create(nums)
        # print(print_tree(root))


if __name__ == '__main__':
    unittest.main()
