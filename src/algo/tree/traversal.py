from src.datastruct.treenode import TreeNode
from typing import Generator
from collections import deque


def preorder_dfs(root: TreeNode) -> Generator:
    if root is None:
        return
    
    yield root.val
    yield from preorder_dfs(root.left)
    yield from preorder_dfs(root.right)


def inorder_dfs(root: TreeNode) -> Generator:
    if root is None:
        return
    
    yield from inorder_dfs(root.left)
    yield root.val
    yield from inorder_dfs(root.right)


def postorder_dfs(root: TreeNode) -> Generator:
    if root is None:
        return
    
    yield from postorder_dfs(root.left)
    yield from postorder_dfs(root.right)
    yield root.val


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
    queue = deque([root])
    while 0 < len(queue):
        node = queue.popleft()
        yield node.val
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def preorder_traversal(root: TreeNode) -> Generator:
    if root is None:
        return
    
    stack = []
    node = root
    while True:
        while node is not None:
            yield node.val
            stack.append(node)
            node = node.left
        
        if len(stack) <= 0:
            break
        node = stack.pop()
        node = node.right


def inorder_traversal(root: TreeNode) -> Generator:
    if root is None:
        return
    
    stack = []
    node = root
    while True:
        while node is not None:
            stack.append(node)
            node = node.left
        
        if len(stack) <= 0:
            break
        node = stack.pop()
        yield node.val
        node = node.right


def postorder_traversal(root: TreeNode) -> Generator:
    if root is None:
        return
    
    stack = []
    visited = None
    node = root
    while True:
        while node is not None:
            stack.append(node)
            node = node.left
        
        if len(stack) <= 0:
            break
        
        if stack[-1].right != visited:
            node = stack[-1].right
            visited = None
        else:
            visited = stack.pop()
            yield visited.val


def levelorder_traversal(root: TreeNode) -> Generator:
    if root is None:
        return
    
    queue = deque([root])
    while 0 < len(queue):
        qsize = len(queue)
        qlevel = []
        for _ in range(qsize):
            node = queue.popleft()
            qlevel.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        yield qlevel
