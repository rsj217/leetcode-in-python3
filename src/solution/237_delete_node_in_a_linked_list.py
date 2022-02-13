from src.datastruct.linknode import ListNode
import unittest


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        """
        node.val = node.next.val
        node.next = node.next.next

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([4, 5, 1, 9], 5, [4, 1, 9]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, val, answer in self.test_case:
            head = ListNode.create(nums)
            node = head
            while node is not None:
                if node.val == val:
                    break
                else:
                    node = node.next
            self.s.deleteNode(node)
            self.assertListEqual(answer, head.to_list())


if __name__ == '__main__':
    unittest.main()
