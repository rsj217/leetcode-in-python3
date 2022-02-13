"""
`Problem <https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/>`_
-------------------------------------------------------------------------------------

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

::

    示例 1：
    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]

    示例 2：

    输入：head = [1], n = 1
    输出：[]

    示例 3：

    输入：head = [1,2], n = 1
    输出：[1]

Tips
------


Answer
--------
"""

from src.datastruct.linknode import ListNode
from typing import Optional
import unittest


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodei, nodej = list1, list2
        head = ListNode()
        prev = head
        while nodei is not None and nodej is not None:
            if nodei.val < nodej.val:
                prev.next = nodei
                prev = prev.next
                nodei = nodei.next
            else:
                prev.next = nodej
                prev = prev.next
                nodej = nodej.next

        while nodei is not None:
            prev.next = nodei
            prev = prev.next
            nodei = nodei.next

        while nodej is not None:
            prev.next = nodej
            prev = prev.next
            nodej = nodej.next

        return head.next
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 4], [1, 3, 4], [1,1,2,3,4,4]),
            ([], [], []),
            ([], [0], [0]),
        ]
        self.s = Solution()

    def test_solution(self):
        for l1, l2, answer in self.test_case:
            list1 = ListNode.create(l1)
            list2 = ListNode.create(l2)
            ans = self.s.mergeTwoLists(list1, list2)
            if ans is not None:
                self.assertListEqual(answer, ans.to_list())
            else:
                self.assertEqual(answer, [])


if __name__ == '__main__':
    unittest.main()
