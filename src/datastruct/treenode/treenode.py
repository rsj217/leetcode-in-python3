"""
树节点&树结构定义，序列化/反序列化，打印，遍历相关算法

"""

from typing import List
from collections import deque
import unittest
import random


class TreeNode:
    """ 树节点(TreeNode)定义，三个字段

    * val： 数据域，通常是 i32。
    * left：左子树，TreeNode 类型
    * right：右子树, TreeNode 类型

    """

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
        """ 树高属性，已当前节点为root的树的树高
        ::

            >>> from src.datastruct.treenode.treenode import TreeNode
            >>> root = TreeNode(val=1)
            >>> height = root.height
        """
        return self._get_height(self)

    def _get_height(self, node) -> int:
        """ 树高的求法，递归DFS方法。
        即 ``curnode.height = 1 + max(node.left.height, node.right.height)``
        空树（empty tree）定义高度为0
        """
        if not node:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    @classmethod
    def create(cls, nums: List[int]):
        """ ``create`` 方法用于将的正数列表反序列化成一棵树。
        列表元素的的顺序是树的 `BFS` 层序遍历的顺序
        除了最深的一层的叶子节点之外，其他的叶子节点的左右子树，使用 ``None`` 站位。位于最后一个节点之后的 ``None`` 则需要去掉
        该方法与 ``literal`` 逆方法。后者将一棵树序列化成整数列表。
        实现原理借助了完全二叉树层序遍历的序号(seq) 与 数组中索引(index)的关系。
        由于有的None节点在数组中不存在，因此这个 seq 与 完全二叉树的节点 seq 有差别。但左右子树的序号与当前节点的序号关系依然成立

        ::

            nums = [
                1,
                2, 3,
                4, None, 5, 6,
                None, 7, None, None, 8,
            ]
            root = TreeNode.create(nums)

        root 的拓扑形状如下，可以使用该模块的 ``print_tree`` 打印树的拓扑

        ::

                   1
               2       3
             4       5   6
              7         8

        叶子节点 2 的右子树，4的左子树 5 的左右子树都用 None 占位，叶子节点 6 的右子树在最后一个节点 8 之后，就不需要 None 占位了。
        树的序列化和反序列化可以参考 Leetcode `[297.二叉树序列化] <https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/>`_
        """

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

    @classmethod
    def literal(cls, root) -> List[int]:
        """
        ``literal`` 是将一颗二叉树序列化成整数列表。是 ``create`` 方法的逆方法。
        其原理是使用二叉树的 `bfs` 层序遍历依次解析节点。
        从树根开始遍历，如果当前节点不存在，直接放入输出 ``None`` 进行占位。如果节点存在，则将其值输出到结果。
        遍历完成之后，再剔除最后一个节点之后的 ``None`` 值。

        ::

            from src.datastruct.treenode import TreeNode
            nums = [
                1, 2, 3, 4, None, 5, 6, None, 7, None, None, 8,
            ]
            root = TreeNode.create(nums)
            ans = TreeNode.literal(root)
            assert nums, ans, "err"
        """

        if root is None:
            return []

        queue = deque()
        queue.append(root)
        ans = []
        while len(queue) > 0:
            qsize = len(queue)
            for i in range(qsize):
                node = queue.popleft()
                if node is not None:
                    ans.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    ans.append(None)

        size = len(ans)
        for i in range(size - 1, -1, -1):
            if ans[i] is None:
                ans.pop()
            else:
                break
        return ans


def print_tree(node) -> str:
    """ 打印二叉树的拓扑形状，调用两个子函数，
    分表是 dfs 方法和 bfs 方法，两个方法随机调用
    """

    num = random.randint(0, 1)
    d = {
        0: print_tree_dfs,
        1: print_tree_bfs,
    }
    ans = d[num](node)
    return "\n".join(["".join(line) for line in ans])


def print_tree_dfs(node: TreeNode) -> List[List[str]]:
    """
    ``print_tree_dfs`` 函数用于打印二叉树的树形拓扑，方便直观的观察一棵树的形状。便于验证相关树算法。

    拓扑结果中，并没有画出路径，由于控制台输出长度的限制，树的节点数也有限制。树的宽度 ``width = (1<<height) - 1`` ，不能太大。
    函数使用了 ``DFS`` 方式遍历一棵树。
    """

    if node is None:
        return []

    height = node.height
    width = (1 << height) - 1
    ans = [[" " for _ in range(width)] for _ in range(height)]

    def dfs(node: TreeNode, deep: int, lo: int, hi: int):
        if node is None:
            return
        mid = lo + (hi - lo) // 2
        ans[deep][mid] = str(node.val)
        dfs(node.left, deep + 1, lo, mid)
        dfs(node.right, deep + 1, mid + 1, hi)

    dfs(node, 0, 0, width)
    return ans


def print_tree_bfs(node: TreeNode) -> List[List[str]]:
    """ 使用 bfs 方法打印二叉树的树形拓扑
    """
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



class TestTreeNode(unittest.TestCase):

    def test_create(self):
        nums = []
        root = TreeNode.create(nums)
        self.assertIsNone(root)
        self.assertEqual(nums, TreeNode.literal(root))

        nums = [1, 2, 3]
        root = TreeNode.create(nums)
        self.assertEqual(nums, TreeNode.literal(root))

        nums = [1, None, 2, 3]
        root = TreeNode.create(nums)
        self.assertEqual(nums, TreeNode.literal(root))

        nums = [1, 2, 3, None, 4, 5]
        root = TreeNode.create(nums)
        self.assertEqual(nums, TreeNode.literal(root))

        nums = [1, 2, 3, None, None, 5]
        root = TreeNode.create(nums)
        self.assertEqual(nums, TreeNode.literal(root))

        nums = [1, 2, 3, None, None, 5, None, 6]
        root = TreeNode.create(nums)
        self.assertEqual(nums, TreeNode.literal(root))


class TestPrintTreeNode(unittest.TestCase):

    def test_empty(self):
        root = TreeNode.create([])
        print(print_tree(root))

    def test_print_tree(self):
        root = TreeNode.create([1, 2, 3, 4, None, 5, 6, None, 7, None, None, 8])
        print(print_tree(root))

        nums = [1, None, 2, 3]
        root = TreeNode.create(nums)
        print(print_tree(root))

        nums = [1, 2, None, 3]
        root = TreeNode.create(nums)
        print(print_tree(root))

        nums = [1, 2, 3, None, 4, 5]
        root = TreeNode.create(nums)
        print(print_tree(root))

        nums = [1, 2, 3, None, None, 5]
        root = TreeNode.create(nums)
        print(print_tree(root))

        nums = [1, 2, 3, None, None, 5, None, 6]
        root = TreeNode.create(nums)
        print(print_tree(root))


if __name__ == '__main__':
    unittest.main()
