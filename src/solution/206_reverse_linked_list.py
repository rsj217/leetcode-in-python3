from typing import List

import unittest
from src.datastruct.linknode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node is not None:
            next_ = node.next
            node.next = prev
            prev = node
            node = next_
        return prev


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
            head = ListNode.create(nums)
            ans = self.s.reverseList(head)
            self.assertListEqual(answer, ans.to_list())


if __name__ == '__main__':
    unittest.main()
