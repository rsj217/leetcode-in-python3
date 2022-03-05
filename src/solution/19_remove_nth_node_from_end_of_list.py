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
import unittest


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        head_ = ListNode()
        head_.next = head

        i = 0
        fast = head
        slow = None
        while fast is not None:
            if i < n:
                i += 1
            elif i == n:
                slow = head
                i += 1
            else:
                slow = slow.next
            fast = fast.next
        if slow is None:
            return head.next

        next_ = slow.next
        if next_ is not None:
            slow.next = next_.next
        return head_.next


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
            ([1], 1, []),
            ([1, 2], 1, [1]),
            ([1, 2], 2, [2]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, n, answer in self.test_case:
            head = ListNode.deserialize(nums)
            ans = self.s.removeNthFromEnd(head, n)
            if ans is not None:
                self.assertListEqual(answer, ListNode.serialize(ans))
            else:
                self.assertEqual(answer, [])


if __name__ == '__main__':
    unittest.main()
