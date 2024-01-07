from src.datastruct.treenode import TreeNode
from typing import Generator
from collections import deque


def preorder_dfs(root: TreeNode) -> Generator:
    if root is None:
        return
    
    yield root.val
    yield from preorder_dfs(root.left)
    yield from preorder_dfs(root.right)


def dfs(root: TreeNode) -> Generator:
    if root is None:
        return
    stack = [root]
    while 0 < len(stack):
        node = stack.pop()
        yield node.val
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


def bfs(root: TreeNode) -> Generator:
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while 0 < len(queue):
        node = queue.popleft()
        yield node.val
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
