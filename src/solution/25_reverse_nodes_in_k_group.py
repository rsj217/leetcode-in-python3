"""
`Problem <https://leetcode-cn.com/problems/reverse-nodes-in-k-group/>`_
-------------------------------------------------------------------------------------
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


::

    示例 1：

    输入：head = [1,2,3,4,5], k = 2
    输出：[2,1,4,3,5]

    示例 2：

    输入：head = [1,2,3,4,5], k = 3
    输出：[3,2,1,4,5]

    示例 3：

    输入：head = [1,2,3,4,5], k = 1
    输出：[1,2,3,4,5]

    示例 4：

    输入：head = [1], k = 1
    输出：[1]

    提示：

    列表中节点的数量在范围 sz 内
    1 <= sz <= 5000
    0 <= Node.val <= 1000
    1 <= k <= sz

Tips
------


Answer
--------
"""

from typing import Optional
from src.datastruct.linknode import ListNode
import unittest


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        head_ = head
        next_ = head
        for i in range(k):
            if next_ is not None:
                next_ = next_.next
            else:
                # 不足 k 个
                return head_

        # k 个reverse
        prev = None
        node = head
        for i in range(k):
            t = node.next
            node.next, prev, node = prev, node, t

        # k 个 reverse 后连接 递归结果
        head.next = self.reverseKGroup(next_, k)
        return prev


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
            ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
            ([1, 2, 3, 4, 5], 4, [4, 3, 2, 1, 5]),
            ([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1]),
            ([1], 1, [1]),
        ]
        self.s = Solution()

    def test_solution(self):
        for num, k, answer in self.test_case:
            node = ListNode.create(num)
            ans = self.s.reverseKGroup(node, k)
            self.assertListEqual(answer, ans.to_list())


if __name__ == '__main__':
    unittest.main()
