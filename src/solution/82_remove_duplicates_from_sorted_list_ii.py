"""
`Problem <https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/>`_
-----------------------------------------------------------------------------------------

82. 删除排序链表中的重复元素II

给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

::

    示例 1：

.. image:: ../../img/82-1.jpeg


::

    输入：head = [1,2,3,3,4,4,5]
    输出：[1,2,5]


.. image:: ../../img/82-2.jpeg

::

    示例 2：

    输入：head = [1,1,1,2,3]
    输出：[2,3]

    提示：

    链表中节点数目在范围 [0, 300] 内
    -100 <= Node.val <= 100
    题目数据保证链表已经按升序 排列

Tips
------

1. 快慢指针
2. 快指针与其自身下一个节点比对  fast.val fast.next.val
3. slow 指针不存在的情况，即删除head的处理, 虚拟头结点 dummy

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
        delete = False
        slow = None
        fast = head
        while fast is not None:
            if fast.next is None:
                if delete:
                    if slow is not None:
                        slow.next = fast.next
                    else:
                        dummy.next = fast.next
                    delete = False
            else:
                if fast.val != fast.next.val:
                    if delete:
                        if slow is not None:
                            slow.next = fast.next
                        else:
                            dummy.next = fast.next
                        delete = False
                    else:
                        slow = fast
                else:
                    delete = True
            fast = fast.next
        return dummy.next


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
            ([1, 1, 2, 3, 3, 4, 4, 5], [2, 5]),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, 1], []),
            ([1, 1, 1, 2, 3], [2, 3]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            head = ListNode.deserialize(nums)
            ans = self.s.deleteDuplicates(head)
            self.assertListEqual(answer, ListNode.serialize(ans))


if __name__ == '__main__':
    unittest.main()
