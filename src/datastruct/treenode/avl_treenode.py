"""
AVL树搜索节点&树结构定义，插入，删除相关遍历相关算法

AVL 树也是二叉搜索树，其插入，删除方法基于二叉搜索插入，删除方法

不同在于插入或删除节点，该节点的祖先节点的高度会发生变化，需要进行选择以调整平衡
"""

import unittest
import random


class AVLTreeNode:
    """ 二叉搜索树节点
    ``AVLTreeNode`` 新增了 ``height`` 属性。提供了节点的插入 ``insert`` 和删除 ``delete`` 操作。
    在插入和删除之后，需要更新节点的 ``height`` 属性。
    通过 ``height`` 计算平衡因子 ``balance factor`` ,当树节点不再平衡的时候，调用旋转 ``_balance_rotate`` 接口维护平衡。
    """

    def __init__(self, key=0):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def minimum(self):
        """ 求最小值节点方法，通过调用 """
        return AVLTreeNode._minimum(self)

    # 为了适配 print_tree 方法
    @property
    def val(self):
        return self.key

    def insert(self, key):
        """ 插入节点方法，当 key 已存在，则更新节点的值，否则将节点插入到 ``AVLTreeNode`` 中 """
        return AVLTreeNode.insert_dfs(self, key)

    def delete(self, key):
        """ 删除节点方法，当 key 不存在，什么也不做 """
        return AVLTreeNode.delete_dfs(self, key)

    @classmethod
    def get_height(cls, node) -> int:
        """ 求节点的树的高度，当节点不存在（空树）时候返回 0
            该方法依次调用其递归方法实现。由于节点本身具有 ``height`` 属性。只需要求左右子树即可，无需过多深入递归。
        """
        if node is None:
            return 0
        return 1 + max(cls.get_height(node.left), cls.get_height(node.right))

    @classmethod
    def get_bf(cls, node):
        """ 求节点的 平衡因子 ``balance_factor = node.left.height - node.right.height`` """
        if node is None:
            return 0
        return cls.get_height(node.left) - cls.get_height(node.right)

    @classmethod
    def _update_height(cls, node):
        """ 更新节点的 ``height`` ，返回更新后的节点 """
        assert node is not None, "node is None"
        height = cls.get_height(node)
        node.height = height
        return node

    @classmethod
    def insert_dfs(cls, node, key):
        """ 以 ``node`` 为根插入 ``key``, 返回插入新的 ``root``
            该方法与 ``二叉树搜索`` 的 ``insert_dfs`` 方法类似，不同在于需要调整平衡。
            插入节点之后，``node`` 的及其 ``parent`` 的路径上的祖先节点高度会变化，需要先更新高度。
            为了保持平衡，需要进行平衡调整，通过旋转得到新子树的子根节点，然后返回给上层递归调用。
        """
        # 插入新节点
        if node is None:
            return AVLTreeNode(key=key)
        # 左子树插入
        if key < node.key:
            node.left = cls.insert_dfs(node.left, key)
        # 右子树插入
        elif node.key < key:
            node.right = cls.insert_dfs(node.right, key)
        else:
            node.key = key
        # 更新当前节点高度
        node = cls._update_height(node)
        # 平衡调整，并返回新的节点作为子树的root，返回给上层调用
        return cls._balance_rotate(node)

    @classmethod
    def delete_dfs(cls, node, key):
        """ 以 ``node`` 为根删除匹配 ``key`` 的节点, 返回删除后新的 ``root``，若 ``key`` 不存在，则不作删除操作。
            该方法与 ``二叉树搜索`` 的 ``delete_dfs`` 方法类似，不同在于需要调整平衡。
            与 ``_insert`` 方法类似，删除节点的祖先节点的高度都会变化，需要更新其高度，并对当前节点为根的子树进行平衡调整。
        """
        # 未匹配 key，不做操作
        if node is None:
            return
        # 递归删除左子树
        if key < node.key:
            node.left = cls.delete_dfs(node.left, key)
        # 递归删除右子树
        elif node.key < key:
            node.right = cls.delete_dfs(node.right, key)
        else:
            # 待删除 key 节点 左右子树都存在。使用右子树的 最小值 替换当前节点。然后删除右子树最小值，并把最小值的右子树嫁接到当前节点
            if node.left is not None and node.right is not None:
                successor = cls._minimum(node.right)
                successor.right = cls.delete_dfs(node.right, key)
                successor.left = node.left
                node = successor
            # 左子树不为空，返回左子树
            if node.left is not None:
                node = node.left
            elif node.right is not None:
                node = node.right
            else: # 左右子树都为空，删除当前节点，即返回None即可
                return None

        # 更新当前节点高度
        node = cls._update_height(node)
        # 平衡调整，并返回新的节点作为子树的root，返回给上层调用
        return cls._balance_rotate(node)

    @classmethod
    def _minimum(cls, node):
        """ 以 ``node`` 为 ``root`` 的AVL树中查找最小值节点 """
        assert node is not None, "node err"
        if node.left is None:
            return node
        return cls._minimum(node.left)

    @classmethod
    def right_rotate(cls, x):
        """ 右旋转
        """
        y = x.left
        T3 = y.right
        y.right = x
        x.left = T3
        # 旋转之后，更新新的树 树高
        cls._update_height(x)
        return cls._update_height(y)

    @classmethod
    def left_rotate(cls, x):
        """ 左旋转
        """
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2

        cls._update_height(x)
        return cls._update_height(y)

    @classmethod
    def _balance_rotate(cls, node):
        """ 平衡调整 一共四种情况

            * LL：
            * LR
            * RR：
            * RL
        """
        bf = cls.get_bf(node)
        if bf > 1:
            # LL
            if cls.get_bf(node.left) >= 0:
                node = cls.right_rotate(node)
            else:  # LR
                node.left = cls.left_rotate(node.left)
                node = cls.right_rotate(node)
        elif bf < -1:
            # RR
            if cls.get_bf(node.right) <= 0:
                node = cls.left_rotate(node)
            else:  # RL
                node.right = cls.right_rotate(node.right)
                node = cls.left_rotate(node)
        return node

    @classmethod
    def is_balance(cls, node) -> bool:
        """ 平衡判断 """
        if node is None:
            return True
        if abs(cls.get_bf(node)) > 1:
            return False
        return cls.is_balance(node.left) and cls.is_balance(node.right)


from src.datastruct.treenode.treenode import print_tree


class TestAVLTreeNode(unittest.TestCase):

    def test_insert_LL(self):
        """
        ::

                3            2
               /            / \\
              2        ->  1   3
             /
            1
        """
        nums = [2, 1]
        avl = AVLTreeNode(3)
        root = avl
        for i in nums:
            root = avl.insert(i)
        self.assertTrue(AVLTreeNode.is_balance(root))

    def test_insert_LR(self):
        """
        ::

                3            2            1
               /            /            / \\
              1        ->  1       ->   2   3
               \\          /
                2        2
        """
        nums = [1, 2]
        avl = AVLTreeNode(3)
        root = avl
        for i in nums:
            root = avl.insert(i)
        self.assertTrue(AVLTreeNode.is_balance(root))

    def test_insert_RR(self):
        """
        ::

            1                 2
             \\               / \\
               2        ->  1   3
                \\
                 3
        """
        nums = [2, 3]
        avl = AVLTreeNode(2)
        root = avl
        for i in nums:
            root = avl.insert(i)
        self.assertTrue(AVLTreeNode.is_balance(root))

    def test_insert_RL(self):
        """
        ::

            1           1            2
             \\           \\          / \\
              2    ->     2    ->  1   3
             /             \\
            3               3
        """
        nums = [1, 2]
        avl = AVLTreeNode(3)
        root = avl
        for i in nums:
            root = avl.insert(i)
        self.assertTrue(AVLTreeNode.is_balance(root))

    def test_delete_one_element(self):
        avl = AVLTreeNode(0)
        avl.delete(10)
        self.assertEqual(avl.key, 0)
        print(print_tree(avl))

        avl = avl.delete(0)
        print(print_tree(avl))
        self.assertIsNone(avl)

    def test_delete_LL(self):
        nums = [2, 4, 1]
        avl = AVLTreeNode(3)
        root = avl
        for i in nums:
            avl.insert(i)
        print(print_tree(root))
        print()
        root = avl.delete(4)
        print(print_tree(root))
        self.assertTrue(AVLTreeNode.is_balance(root))

    def test_delete_LR(self):
        nums = [1, 4, 2]
        avl = AVLTreeNode(3)
        root = avl
        for i in nums:
            avl.insert(i)
        print(print_tree(root))
        print("=" * 20)
        root = avl.delete(4)
        print(print_tree(root))
        self.assertTrue(AVLTreeNode.is_balance(root))

    def test_delete_RR(self):
        nums = [1, 3, 4]
        avl = AVLTreeNode(2)
        root = avl
        for i in nums:
            avl.insert(i)
        print(print_tree(root))
        print()
        root = avl.delete(1)
        print(print_tree(root))
        self.assertTrue(AVLTreeNode.is_balance(root))

    def test_delete_RL(self):
        nums = [1, 4, 3]
        avl = AVLTreeNode(2)
        root = avl
        for i in nums:
            avl.insert(i)
        print(print_tree(root))
        print("=" * 20)
        root = avl.delete(1)
        print(print_tree(root))
        self.assertTrue(AVLTreeNode.is_balance(root))

    def test_random(self):
        nums = list(range(1, 10))
        avl = AVLTreeNode(0)
        root = avl
        for i in nums:
            root = root.insert(i)
        print(print_tree(root))

        for _ in range(len(nums) - 2):
            n = random.randint(nums[0], nums[-1])
            print("=" * 20)
            print(f"delete: {n}")
            root = root.delete(n)
            print("delete after:")
            print(print_tree(root))
            self.assertTrue(AVLTreeNode.is_balance(root))
            print("=" * 20)


if __name__ == '__main__':
    unittest.main()
