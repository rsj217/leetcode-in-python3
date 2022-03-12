"""
`Problem <https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/>`_
-----------------------------------------------------------------------------

83. 删除排序链表中的重复元素

给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

::

    示例 1：

    输入：head = [1,1,2]
    输出：[1,2]

    示例 2：

    输入：head = [1,1,2,3,3]
    输出：[1,2,3]


Tips
------

1. 快慢指针，快指针和慢指针同步
2. 比对 fast和fast.next

Answer
------

"""

from src.datastruct.linknode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        dummy = ListNode()
        dummy.next = head
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            if fast.val == fast.next.val:
                slow.next = fast.next.next
            else:
                slow = slow.next
                fast = fast.next

        return dummy.next


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 3, 4, 4, 5], [1, 2, 3, 4, 5]),
            ([1, 1, 2, 3, 3, 4, 4, 5], [1, 2, 3, 4, 5]),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, 1], [1]),
            ([1, 1, 1, 2, 3], [1, 2, 3]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            head = ListNode.deserialize(nums)
            ans = self.s.deleteDuplicates(head)
            self.assertListEqual(answer, ListNode.serialize(ans))


if __name__ == '__main__':
    unittest.main()
