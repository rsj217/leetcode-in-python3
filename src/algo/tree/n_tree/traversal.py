from src.datastruct.n_treenode import NTreeNode
from typing import Generator
from collections import deque


def preorder(root: NTreeNode) -> Generator:
    if root is None:
        return
    yield root.val
    for child in root.children:
        yield from preorder(child)


def postorder(root: NTreeNode) -> Generator:
    if root is None:
        return
    for child in root.children:
        yield from postorder(child)
    yield root.val


def preorder_traversal(node: NTreeNode) -> int:
    if node is None:
        return
    stack = [node]
    while len(stack) > 0:
        node = stack.pop()
        yield node.val
        for i in range(len(node.children) - 1, -1, -1):
            stack.append(node.children[i])
