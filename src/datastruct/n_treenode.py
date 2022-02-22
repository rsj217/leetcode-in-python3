""" N 叉树 节点定义

"""

from __future__ import annotations
import os
from typing import List, Optional
from collections import deque


class NTreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []

    @classmethod
    def serialize(cls, nums: List[int]) -> Optional[NTreeNode]:
        if len(nums) <= 0:
            return None
        root = NTreeNode(val=nums[0])
        queue = deque()
        queue.append(root)
        parent = root

        for i in nums[1:]:
            if i is None:
                parent = queue.popleft()
            else:
                node = NTreeNode(val=i)
                parent.children.append(node)
                queue.append(node)
        del queue
        return root

    @classmethod
    def deserialize(cls, node: NTreeNode) -> List[int]:
        if node is None:
            return []

        ans = [node.val, None]
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            node = queue.popleft()
            for i in node.children:
                ans.append(i.val)
                queue.append(i)
            ans.append(None)

        size = len(ans)
        for i in range(size - 1, -1, -1):
            if ans[i] is None:
                ans.pop()
            else:
                break
        return ans


def preorder_dfs(root: NTreeNode) -> int:
    if root is None:
        return
    yield root.val
    for i in root.children:
        yield from preorder_dfs(i)


def preorder_traversal(node: NTreeNode) -> int:
    if node is None:
        return

    stack = [node]
    while len(stack) > 0:
        node = stack.pop()
        yield node.val
        for i in range(len(node.children) - 1, -1, -1):
            stack.append(node.children[i])


def graphviz_tree(node: NTreeNode):
    if node is None:
        return []

    seq = 0
    lines = []
    lines.append('digraph g {')
    lines.append('node [shape=record, height=.1];\n')
    lines.append(f'node{seq}[label="{node.val}"];\n')

    queue = [(node, f'node{seq}')]

    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            node, parent = queue.pop(0)
            for i in node.children:
                seq += 1
                queue.append((i, f'node{seq}'))
                lines.append(f'node{seq}[label="{i.val}"];\n')
                lines.append(f'{parent} -> node{seq};\n')

    lines.append('}')
    with open("ntree.dot", "w") as f:
        f.writelines(lines)
    cmd = "dot -Tpng -o ntree.png ntree.dot"
    os.system(cmd)
    os.system("open ntree.png")


import unittest


class TestNTreeNode(unittest.TestCase):

    def test_create_literal(self):
        test_case = [
            [],
            [1, None, 3, 2, 4, None, 5, 6],
            [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None,
             None, 14],
        ]

        for nums in test_case:
            root = NTreeNode.serialize(nums)
            ans = NTreeNode.deserialize(root)
            self.assertEqual(nums, ans)
            # graphviz_tree(root)

if __name__ == '__main__':
    unittest.main()
