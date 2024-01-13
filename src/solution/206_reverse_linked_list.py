import random
from typing import Optional
from src.datastruct.linknode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        num = random.randint(0, 1)
        d = {
            0: self.reverse_iterator,
            1: self.reverse_recursion,
        }
        
        return d[num](head)
    
    def reverse_iterator(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node is not None:
            next_ = node.next
            node.next = prev
            prev = node
            node = next_
        return prev
    
    def reverse_recursion(self, head: ListNode) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        reverse_list = self.reverse_recursion(head.next)
        head.next.next = head
        head.next = None
        return reverse_list


import unittest


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
            ([1], [1]),
            ([1, 2], [2, 1])
        ]
        self.s = Solution()
    
    def test_solution(self):
        for nums, answer in self.test_case:
            head = ListNode.deserialize(nums)
            ans = self.s.reverseList(head)
            self.assertListEqual(answer, ListNode.serialize(ans))


if __name__ == '__main__':
    unittest.main()
