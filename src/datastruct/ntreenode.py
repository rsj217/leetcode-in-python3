from typing import List
from collections import deque
import unittest
import random


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []


def create_n_tree():
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node3.children.extend([node5, node6])
    root.children.extend([node3, node2, node4])
    return root

def preorder(root:TreeNode):
    if root is None:
        return
    print(root.val)
    for i in root.children:
        preorder(i)


def levelorder(root:TreeNode):
    from treenode import TreeNode
    q = [root]
    while len(q)> 0:
        size = len(q)
        qq = []
        for i in range(size):
            node = q[i]
            print(node.val)
            qq.extend(node.children)

        q = qq

if __name__ == '__main__':
    root = create_n_tree()
    # preorder(root)
    node = levelorder(root)
    from treenode import print_tree
    s = print_tree(node)
    print(s)

