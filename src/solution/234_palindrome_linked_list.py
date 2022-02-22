"""
`Problem <https://leetcode-cn.com/problems/palindrome-linked-list/>`_
-----------------------------------------------------------------------------
234. 回文链表

给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

::

    示例 1：

    输入：head = [1,2,2,1]
    输出：true

    示例 2：

    输入：head = [1,2]
    输出：false

    提示：


    链表中节点数目在范围[1, 10⁵] 内
    0 <= Node.val <= 9

    进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

Tips
------

1. 快慢指针，找到中点
2. 根据 fast 是否存在，判定中点是正中还是偏右
3. 反转右边部分，正中的从下一个节点开始反转，偏右从当前节点开始反转
4. 比对左边和反转的右边，判定结构

Answer
------
"""

from src.datastruct.linknode import ListNode
import unittest


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # 快慢指针找中点
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        # 判定中点偏右还是正中
        if fast is not None:
            node = slow.next
        else:
            node = slow

        # 反转右边
        prev = None
        while node is not None:
            next_ = node.next
            node.next = prev
            prev = node
            node = next_

        # 比对左边和右边
        head_ = prev
        while head_ is not None:
            if head_.val != head.val:
                return False
            head = head.next
            head_ = head_.next
        return True


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 2, 1], True),
            ([1, 2, 3, 1, 2], False),
            ([1, 2, 2, 1], True),
            ([1, 2, 3, 1], False),
            ([1], True),
            ([1, 2], False),
            ([1, 1], True),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            head = ListNode.create(nums)
            ans = self.s.isPalindrome(head)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
