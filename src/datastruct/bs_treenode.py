"""
二叉树搜索节点&树结构定义，插入，删除相关算法

* 节点的左子树只包含小于当前节点的数。
* 节点的右子树只包含大于当前节点的数。
* 所有左子树和右子树自身必须也是二叉搜索树。

"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List
import unittest
from src.algo.sort import helper
from src.datastruct.treenode import print_tree


@dataclass
class BSTreeNode:
    """ 二叉搜索树节点
        通常二叉搜索树的数据域是 ``（key，val）`` 这样的数据结构。``key`` 用于排序，``val`` 存储实际的值
        二叉树搜索树的 ``insert`` 和 ``delete`` 算法都不涉及 ``val`` 操作
        为了描述算法，``BSTreeNode`` 节点定义只有 ``key`` 和左( ``left`` )右( ``right`` )子树
    """
    
    key: int = 0
    left: BSTreeNode = None
    right: BSTreeNode = None
    
    @property
    def val(self):
        """ val 属性是为了匹配 ``print_tree`` 方法"""
        return self.key
    
    @property
    def height(self):
        """ 树高属性，已当前节点为root的树的树高 """
        return self._get_height(self)
    
    def _get_height(self, node: BSTreeNode) -> int:
        """ 树高的求法，递归DFS方法。
        即 ``curnode.height = 1 + max(node.left.height, node.right.height)``
        空树（empty tree）定义高度为0
        """
        if not node:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))
    
    def insert(self, key: int) -> BSTreeNode:
        """插入值为 ``key`` 的节点"""
        return BSTreeNode.insert_dfs(self, key)
    
    def delete(self, key: int) -> BSTreeNode:
        """删除值为 ``key`` 的节点"""
        return BSTreeNode.delete_dfs(self, key)
    
    @classmethod
    def minimum_dfs(cls, node: BSTreeNode) -> BSTreeNode:
        """ 以 ``node`` 为 ``root`` 的二叉搜索树中查找最小值节点 """
        if node.left is None:
            return node
        return cls.minimum_dfs(node.left)
    
    @classmethod
    def delete_dfs(cls, node: BSTreeNode, key: int) -> BSTreeNode:
        """ delete_dfs 方法，递归使用 ``dfs`` 删除以 ``node`` 为根的二叉搜素中的 ``key`` 的节点。 若节点不存在，则什么也不做
            通过递归调用左右子树，返回删除节点之后的新树的树根
            删除一个 ``key``  节点，有三种情况

            * key 节点是叶子节点：直接删除，返回 ``None`` 给上层递归调用
            * key 节点只有一个子树。如有左子树，无右子树。返回右子树，另外一种情况对称
            * key 节点左右子树都存在。找到 ``key`` 节点的右子树，以右子树为根找到其最小值。
                  也就是 ``key`` 的后继节点 ``successor`` ， 然后把这个 ``successor`` 和 ``key`` 互换
                  接下来再删除 ``key`` 节点，也就是退化为删除只有右子树，而无左子树的情况
        """
        # 未找到 key 值，不删除
        if node is None:
            return node
        
        if node.key < key:
            node.right = cls.delete_dfs(node.right, key)
        elif key < node.key:
            node.left = cls.delete_dfs(node.left, key)
        else:  # node.key == key
            # 左右子树都存在，删除key节点右子树的最小值
            if node.left is not None and node.right is not None:
                successor = cls.minimum_dfs(node.right)
                successor.right = cls.delete_dfs(node.right, successor.key)
                successor.left = node.left
                node = successor
            elif node.left is not None:
                lnode = node.left
                node.left = None
                return lnode
            elif node.right is not None:
                rnode = node.right
                node.right = None
                return rnode
            else:
                return None
        return node
    
    @classmethod
    def insert_dfs(cls, node: BSTreeNode, key: int) -> BSTreeNode:
        """ 以 ``node`` 为 ``root`` 的二叉搜索树中插入 ``key``，并返回新的 ``root`` """
        if node is None:
            return BSTreeNode(key)
        if key < node.key:
            node.left = cls.insert_dfs(node.left, key)
        elif node.key < key:
            node.right = cls.insert_dfs(node.right, key)
        else:
            node.key = key
        return node


class BSTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = BSTreeNode(key)
        else:
            self.root = BSTreeNode.insert_dfs(self.root, key)
    
    def delete(self, key):
        if self.root is None:
            return
        self.root = BSTreeNode.delete_dfs(self.root, key)


def is_valid(node: BSTreeNode) -> bool:
    nums = inorder_dfs(node)
    return helper.is_sorted(nums)


def inorder_dfs(node) -> List[int]:
    """ 中序遍历 """
    
    def dfs(node) -> List[int]:
        if node is None:
            return
        yield from dfs(node.left)
        yield node.key
        yield from dfs(node.right)
    
    return list(dfs(node))


class TestBSTreeNode(unittest.TestCase):
    
    def test_insert(self):
        nums = [5, 2, 3, 7, 8, 9, 1]
        root = BSTreeNode()
        for i in nums:
            root.insert(i)
        self.assertTrue(is_valid(root))
    
    def test_delete_leaf(self):
        nums = [2, 1, 3]
        root = BSTreeNode(4)
        for i in nums:
            root.insert(i)
        print(print_tree(root))
        self.assertTrue(is_valid(root))
        print()
        
        root = root.delete(1)
        print(print_tree(root))
        self.assertTrue(is_valid(root))
    
    def test_delete_left_child(self):
        nums = [2, 1, 3]
        root = BSTreeNode(4)
        for i in nums:
            root.insert(i)
        print(print_tree(root))
        self.assertTrue(is_valid(root))
        print()
        
        root = root.delete(4)
        print(print_tree(root))
        self.assertTrue(is_valid(root))
    
    def test_delete_right_child(self):
        nums = [2, 3]
        root = BSTreeNode(4)
        for i in nums:
            root.insert(i)
        print(print_tree(root))
        self.assertTrue(is_valid(root))
        print()
        
        root = root.delete(2)
        print(print_tree(root))
        self.assertTrue(is_valid(root))


if __name__ == '__main__':
    unittest.main()
