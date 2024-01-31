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

1. 快慢指针，找到中点，同时翻转左边
2. 根据 fast 是否存在，判定中点是正中还是偏右
3. 比对左边和反转的右边，判定结构

```
1--->2--->3--->2--->1-->

1<---2<---3--->2--->1-->
     |    |         |
    prev slow      fast


1--->2--->2--->1-->

1<---2--->2--->1-->none
     |    |         |
    prev slow      fast
```

Answer
------
"""

from src.datastruct.linknode import ListNode
import unittest


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        fast = head
        slow = head
        prev = None
        
        # 快慢指针找中点，同时 reverse 左边链表
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            # 翻转左边
            next_ = slow.next
            slow.next = prev
            prev = slow
            slow = next_
        
        # 判定中点偏右还是正中
        left = prev
        if fast is not None:
            right = slow.next
        else:
            right = slow
        
        # 从中间相两边比较
        while left is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
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
            head = ListNode.deserialize(nums)
            ans = self.s.isPalindrome(head)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
