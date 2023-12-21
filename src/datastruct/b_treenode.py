from __future__ import annotations

import unittest
from typing import Optional
import collections
import os


def find(nums, key):
    """ 查找 nums 中，不大于 key 的最大 index """
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] <= key:
            return i
    return -1


class BTreeNode:

    def __init__(self):
        self.parent = None
        self.keys = []
        self.children = [None]

    def __str__(self) -> str:
        keys = [str(i) for i in self.keys]
        val = "|".join(keys)
        return f"|{val}|"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def search_dfs(cls, node: Optional[BTreeNode], key: int, hot: Optional[BTreeNode]) -> (BTreeNode, BTreeNode):
        """
        search_dfs 内部搜索接口，以 node 为根节点进行 关键码 key 的查找。
        因为树由内部节点和外部节点组成，外部节点都是 None 空引用。因此节点一定会命中。
        hot 则表示命中节点的 parent 节点。
        """
        if node is None:
            return hot, node

        r = find(node.keys, key)
        if (0 <= r) and node.keys[r] == key:
            return hot, node
        hot = node
        node = node.children[r + 1]
        return cls.search_dfs(node, key, hot)

    @classmethod
    def minimum_dfs(cls, node: BTreeNode) -> BTreeNode:
        if node.children[0] is None:
            return node
        return cls.minimum_dfs(node.children[0])

    @staticmethod
    def _search(node: BTreeNode, key: int) -> (BTreeNode, BTreeNode):
        parent = None
        while node is not None:
            r = find(node.keys, key)
            if (0 <= r) and node.keys[r] == key:
                return parent, node
            parent = node
            node = node.children[r + 1]
        return parent, node

    @classmethod
    def insert(cls, node: BTreeNode, key: int, order: int) -> BTreeNode:
        """
        以 node 为 root 插入关键码 key，返回插入之后新树的root。
        先使用 search_dfs 查找，目标 key 已存在则直接返回，否则将目标 key 插入到 叶子节点。
        当叶子节点新增一个key之后，其自身的 key 的个数可能上溢 overflow，需要调用 overflow_split 方法修复上溢的节点
        """
        hot, ans = cls.search_dfs(node, key, None)
        if ans is not None:
            return node
        r = find(hot.keys, key)
        hot.keys.insert(r + 1, key)
        hot.children.insert(r + 2, None)
        return cls.overflow_split(node, hot, order)

    @classmethod
    def delete(cls, node: BTreeNode, key: int, order: int) -> BTreeNode:
        """
        以 node 为 root，删除关键码 key ，返回删除后新树的树root
        与 insert 类似，先查找目标 key，若 key 不存在，则忽略。
        当查找到 key 之后。如果 key 是root，则root跟其中序后继的节点进行交换，进而删除交换后的中序后继节点 successor。
        如果 key 不是 根节点，则删除相应节点的key。
        删除 key 之后节点key 数量减少，可能发现下溢（underflow），需要调用 underflow_merge 方法修复下溢节点。
        """
        _, ans = cls.search_dfs(node, key, None)
        if ans is None:
            return node
        r = find(ans.keys, key)
        if ans.children[0] is not None:  # 目标节点是非叶子节点
            successor = cls.minimum_dfs(ans.children[r + 1])  # 查找中序后继 sucessor：右孩子的最左边的节点
            ans.keys[r] = successor.keys[0]  # 与 successor 节点交换 key
            ans = successor  # 将目标转换为删除 successor
            r = 0
        ans.keys.pop(r)
        ans.children.pop(r + 1)
        return cls.underflow_merge(node, ans, order)  # 删除节点可能发生下溢，通过旋转或合并修复

    @classmethod
    def overflow_split(cls, root: BTreeNode, node: BTreeNode, order: int) -> BTreeNode:

        if len(node.children) <= order:  # 递归基：当前节点node的children 小于等于order的时候，节点未发生overflow
            return root
        mid = order // 2  # 中位数节点

        right = BTreeNode()  # 新建一个空节点，为以中位数节点分离的右节点
        right.keys = node.keys[mid + 1:]
        right.children = node.children[mid + 1:]
        node.keys = node.keys[:mid + 1]
        node.children = node.children[:mid + 1]

        if right.children[0] is not None:  # 若 right 的children 不为None，需要更新他们的parent，之前是 node，现在更新为 right
            for i in range(order - mid):
                right.children[i].parent = right

        p = node.parent
        left = node
        if p is None:  # p 不存在，则表示 node 是根节点
            p = BTreeNode()  # 分裂之后，需要一个新的根节点 p
            p.children[0] = left  # node 作为新根 p 的左孩子节点
            left.parent = p
            root = p

        r = 1 + find(p.keys, left.keys[0])  # 找到 p 中指向原 node 的r，用于插入分裂的 mid
        p.keys.insert(r, left.keys.pop(mid))  # p 插入 mid 的 key
        p.children.insert(r + 1, right)  # p 插入 mid 的 children
        right.parent = p  # 更新 分裂 的 right的 parent
        return cls.overflow_split(root, p, order)  # 当前层分裂完毕，向上递归，至多  O(H)，即 O(logN))

    @classmethod
    def underflow_merge(cls, root: BTreeNode, node: BTreeNode, order: int) -> BTreeNode:
        if (order + 1) // 2 <= len(node.children):  # 递归基：当前节点满足最小关键码的大小 [m+1//2, m-1]
            return root

        p = node.parent
        if p is None:
            if len(node.keys) <= 0 and node.children[0] is not None:
                root = node.children[0]
                root.parent = None
                node.children[0] = None
            return root

        r = 0
        while p.children[r] is not node:  # 寻找 node 在 其 parent children中的 rank
            r += 1
        # case1: 左顾：向左兄弟借key 旋转
        if 0 < r:  # 存在左兄弟
            ls = p.children[r - 1]  # ls: left sibling 左兄弟
            if (order + 1) // 2 < len(ls.children):  # ls 可以借出关键码
                node.keys.insert(0, p.keys[r - 1])  # node 从 parent 借出关键码
                p.keys[r - 1] = ls.keys.pop(-1)  # parent 从 ls 借出关键码
                node.children.insert(0, ls.children.pop(-1))  # ls 借出关键码的 children（最右的children） 过继给 node（最左边的children）
                if node.children[0] is not None:  # 借出的 children 非叶子节点，
                    node.children[0].parent = node  # 则需要更新该节点的 parent 为 node
                return root

        # case2: 右盼：向右兄弟借key 旋转
        if r < (len(p.children) - 1):  # 存在有兄弟
            rs = p.children[r + 1]  # rs: right sibling 右兄弟
            if (order + 1) // 2 < len(rs.children):  # rs 可以借出关键码
                node.keys.append(p.keys[r])  # node 从 parent 借出关键码
                p.keys[r] = rs.keys.pop(0)  # parent 从 rs 借出关键码
                node.children.append(rs.children.pop(0))  # 从 rs 借出关键码的 children（最左边的children）过继给 node （最右边的children）
                if node.children[-1] is not None:  # 借出的 children 非叶子节点，
                    node.children[-1].parent = node  # 则需要更新该节点的 parent 为 node
                return root
        # case3: 合并: 左右兄弟都不足以借出
        if 0 < r:  # 与左兄弟合并
            ls = p.children[r - 1]
            ls.keys.append(p.keys.pop(r - 1))
            p.children.pop(r)
            ls.children.append(node.children.pop(0))
            if ls.children[-1] is not None:
                ls.children[-1].parent = ls

            while len(node.keys) > 0:
                ls.keys.append(node.keys.pop(0))
                ls.children.append(node.children.pop(0))
                if ls.children[-1] is not None:
                    ls.children[-1].parent = ls

        else:  # 与右兄弟合并
            rs = p.children[r + 1]
            rs.keys.insert(0, p.keys.pop(r))
            p.children.pop(r)
            rs.children.insert(0, node.children.pop(-1))
            if rs.children[0] is not None:
                rs.children[0].parent = rs
            while len(node.keys) > 0:
                rs.keys.insert(0, node.keys.pop(-1))
                rs.children.insert(0, node.children.pop(-1))
                if rs.children[0]:
                    rs.children[0].parent = rs

        # 合并之后, 高度减少，需要向上回溯，依次修复下溢的节点
        return cls.underflow_merge(root, p, order)


class BTree:
    def __init__(self, order: int = 3):
        self.order = order
        self.root = BTreeNode()

    def search(self, key) -> Optional[int]:
        return BTreeNode.search(self.root, key)

    def insert(self, key: int):
        self.root = BTreeNode.insert(self.root, key, self.order)

    def delete(self, key: int):
        self.root = BTreeNode.delete(self.root, key, self.order)



class TestBTreeNode(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_empty(self):
        node = BTreeNode()
        self.assertIsNone(node.parent)
        self.assertEqual(len(node.keys), 0)
        self.assertEqual(len(node.children), 1)

    def test_insert(self):
        order = 3
        root = BTreeNode()
        root = BTreeNode.insert(root, 53, order)
        self.assertIsNone(root.parent)
        self.assertEqual(root.keys, [53])
        self.assertEqual(root.children, [None, None])

        root = BTreeNode.insert(root, 36, order)
        self.assertIsNone(root.parent)
        self.assertEqual(root.keys, [36, 53])
        self.assertEqual(root.children, [None, None, None])

        root = BTreeNode.insert(root, 77, order)
        self.assertIsNone(root.parent)
        self.assertEqual(root.keys, [53])
        self.assertEqual(len(root.children), 2)

        left = root.children[0]
        right = root.children[1]

        self.assertEqual(left.parent, root)
        self.assertEqual(left.keys, [36])
        self.assertEqual(len(left.children), 2)

        self.assertEqual(right.parent, root)
        self.assertEqual(right.keys, [77])
        self.assertEqual(len(right.children), 2)


class TestBTree(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_insert_overflow_split(self):
        bt = BTree()
        nums = [53, 36, 77, 97, 19, 41, 51, 75, 79, 89, 84]
        for i in nums:
            bt.insert(i)

        bt.insert(23)
        # graphviz_tree(bt.root)
        node36 = bt.root.children[0]
        node1923 = node36.children[0]
        self.assertEqual(node1923.keys, [19, 23])
        self.assertEqual(node1923.parent, node36)

        bt.insert(29)

        node2336 = bt.root.children[0]
        node19, node29, node4151 = node2336.children
        self.assertEqual(node19.parent, node2336)
        self.assertEqual(node19.keys, [19])

        self.assertEqual(node29.parent, node2336)
        self.assertEqual(node29.keys, [29])

        self.assertEqual(node4151.parent, node2336)
        self.assertEqual(node4151.keys, [41, 51])

        bt.insert(45)

        root = bt.root
        self.assertIsNone(root.parent)
        self.assertEqual(root.keys, [36, 53])

        node23, node45, node7789 = root.children

        self.assertEqual(node23.parent, root)
        self.assertEqual(node23.keys, [23])

        self.assertEqual(node45.parent, root)
        self.assertEqual(node45.keys, [45])

        self.assertEqual(node7789.parent, root)
        self.assertEqual(node7789.keys, [77, 89])

        node41, node51 = node45.children
        self.assertEqual(node41.parent, node45)
        self.assertEqual(node41.keys, [41])

        self.assertEqual(node51.parent, node45)
        self.assertEqual(node51.keys, [51])

        bt.insert(87)
        root = bt.root
        self.assertIsNone(root.parent)
        self.assertEqual(root.keys, [53])

    def test_delete_underflow_merge(self):
        bt = BTree()
        nums = [53, 36, 77, 97, 19, 41, 51, 75, 79, 89, 84, 64]
        for i in nums:
            bt.insert(i)

        bt.delete(41)

        n36 = bt.root.children[0]
        n51 = n36.children[0]
        self.assertEqual(n51.parent, n36)
        self.assertEqual(len(n36.keys), 1)

        bt.delete(53)

        root = bt.root
        self.assertEqual(root.keys, [64])
        n75 = root.children[1].children[0]
        self.assertEqual(n75.keys, [75])
        self.assertEqual(n75.children, [None, None])

        bt.delete(75)

        n7989 = bt.root.children[1]

        n77, n84, n97 = n7989.children
        self.assertEqual(n77.keys, [77])
        self.assertEqual(n77.parent, n7989)

        self.assertEqual(n84.keys, [84])
        self.assertEqual(n84.parent, n7989)

        self.assertEqual(n97.keys, [97])
        self.assertEqual(n97.parent, n7989)

        bt.delete(84)

        n89 = bt.root.children[1]
        n7779 = n89.children[0]
        self.assertEqual(len(n89.children), 2)
        self.assertEqual(n7779.keys, [77, 79])
        self.assertEqual(n7779.parent, n89)

        bt.delete(51)

        n6489 = bt.root
        n1936, n7779, n97 = n6489.children
        self.assertEqual(n1936.keys, [19, 36])
        self.assertEqual(n1936.parent, n6489)

        self.assertEqual(n7779.keys, [77, 79])
        self.assertEqual(n7779.parent, n6489)

        self.assertEqual(n97.keys, [97])
        self.assertEqual(n97.parent, n6489)

    # def test_delete_rotate(self):
    #     bt = BTree(5)
    #     nums = [528, 249, 703, 268, 850, 54, 315, 758, 855, 152, 266, 423, 468, 484, 644, 771, 882, 936, 984, 500, 990]
    #     for i in nums:
    #         bt.insert(i)
    #
    #     bt.delete(266)
    #     bt.delete(644)

    def test_left_rotate(self):
        bt = BTree()
        nums = [53, 36, 77, 97, 19, 41, 10, 75, 79, 89]
        for i in nums:
            bt.insert(i)

        bt.delete(41)

        n19 = bt.root.children[0]
        self.assertEqual(n19.parent, bt.root)
        self.assertEqual(n19.keys, [19])

        n10, n36 = n19.children

        self.assertEqual(n10.parent, n19)
        self.assertEqual(n10.keys, [10])

        self.assertEqual(n36.parent, n19)
        self.assertEqual(n36.keys, [36])

    def test_right_rotate(self):
        bt = BTree()
        nums = [53, 36, 77, 97, 19, 41, 51, 75, 79, 89]
        for i in nums:
            bt.insert(i)

        bt.delete(19)

        n41 = bt.root.children[0]
        self.assertEqual(n41.parent, bt.root)
        self.assertEqual(n41.keys, [41])

        n36, n51 = n41.children
        self.assertEqual(n36.parent, n41)
        self.assertEqual(n36.keys, [36])

        self.assertEqual(n51.parent, n41)
        self.assertEqual(n51.keys, [51])

    def test_right_merge(self):
        bt = BTree(5)
        nums = [528, 249, 703, 850, 54, 315, 758, 855, 152, 266, 423, 468, 484, 644, 771, 882, 936, 984, 500, 990]
        for i in nums:
            bt.insert(i)
        bt.delete(54)

    def test_left_merge(self):
        bt = BTree(5)
        nums = [528, 249, 703, 850, 54, 315, 758, 855, 152, 266, 423, 468, 484, 644, 771, 882, 936, 984, 500, 990]
        for i in nums:
            bt.insert(i)
        bt.delete(644)


if __name__ == '__main__':
    unittest.main()
