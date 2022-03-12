"""
`Problem <https://leetcode-cn.com/problems/reverse-linked-list-ii/>`_
--------------------------------------------------------------------------------------

92. 反转链表II

给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

::

    示例 1：

    输入：head = [1,2,3,4,5], left = 2, right = 4
    输出：[1,4,3,2,5]

    示例 2：

    输入：head = [5], left = 1, right = 1
    输出：[5]

    提示：

    链表中节点数目为 n

    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n

    进阶： 你可以使用一趟扫描完成反转吗？


Tips
------

1. 线性扫描，反转 left，right，反转前记录  left.prev 和 left
2. 反转之后，left 接入 right.next
3. left.prev 不存在，即left=0，直接返回反转后的新head
4. left.prev 存在，left.prev 接入 反转后的新head ，返回 head

Answer
--------

"""

from src.datastruct.linknode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        l = 1
        node = head
        prev = None
        start_prev = None
        start = None
        while node is not None:
            next_ = node.next
            if left <= l <= right:
                if left == l:
                    start_prev = prev
                    start = node

                node.next = prev

                if l == right:
                    start.next = next_
                    if start_prev is None:
                        return node
                    else:
                        start_prev.next = node
                        return head
            l += 1
            prev = node
            node = next_


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
            ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
            ([1, 2, 3, 4, 5], 4, 4, [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 1, 4, [4, 3, 2, 1, 5]),

        ]
        self.s = Solution()

    def test_solution(self):
        for nums, left, right, answer in self.test_case:
            head = ListNode.deserialize(nums)
            ans = self.s.reverseBetween(head, left, right)
            self.assertListEqual(answer, ListNode.serialize(ans))


if __name__ == '__main__':
    unittest.main()
