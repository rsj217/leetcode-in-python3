"""
`Problem <https://leetcode-cn.com/problems/>`_
-----------------------------------------------------------------------------

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的
方法解决这个问题。

::

示例 1：

    输入：root = [1,2,3,null,null,4,5]
    输出：[1,2,3,null,null,4,5]

    示例 2：

    输入：root = []
    输出：[]

    示例 3：

    输入：root = [1]
    输出：[1]

    示例 4：

    输入：root = [1,2]
    输出：[1,2]


    提示：

    树中结点数在范围 [0, 10⁴] 内
    -1000 <= Node.val <= 1000



Tips
------

题解

Answer
------

"""

from src.datastruct.treenode import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        ans = []
        queue = [root]
        while len(queue) > 0:
            lsize = len(queue)
            for _ in range(lsize):
                node = queue.pop(0)
                if node is not None:
                    ans.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    ans.append("None")
        for i in range(len(ans) - 1, -1, -1):
            if ans[i] == "None":
                ans.pop()
            else:
                break
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        levelorder = data.split(",")
        numsize = len(levelorder)
        root = TreeNode(int(levelorder[0]))
        queue = [root]
        index = 0
        while len(queue) > 0:
            lsize = len(queue)
            for i in range(lsize):
                node = queue.pop(0)
                if 2 * index + 1 < numsize and levelorder[2 * index + 1] != "None":
                    node.left = TreeNode(int(levelorder[2 * index + 1]))
                    queue.append(node.left)
                if 2 * index + 2 < numsize and levelorder[2 * index + 2] != "None":
                    node.right = TreeNode(int(levelorder[2 * index + 2]))
                    queue.append(node.right)
                index += 1
        return root


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1,2,3,None,None,4,5], "1,2,3,None,None,4,5", [1,2,3,None,None,4,5]),
            ([1, 2], "1,2", [1, 2]),
            ([1], "1", [1]),
            ([], "", [])
        ]
        self.s = Codec()

    def test_solution(self):
        for nums, serialize, deserialize in self.test_case:
            root = TreeNode.deserialize(nums)
            data = self.s.serialize(root)
            self.assertEqual(data, serialize)
            newroot = self.s.deserialize(data)
            self.assertListEqual(deserialize, TreeNode.serialize(newroot))


if __name__ == '__main__':
    unittest.main()
