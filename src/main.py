from typing import List

from src.datastruct.linknode import ListNode

arr = [0, 1, 2, 3, 4, 5, 6]

root = ListNode.deserialize(arr)


def traversal(node: ListNode):
    def dfs(node: ListNode):
        print(node.val)
        next_node = node.next
        if next_node is not None:
            dfs(next_node)
    
    dfs(node)


def traversal(node: ListNode):
    stack = [node]
    while 0 < len(stack):
        node = stack.pop()
        print(node.val)
        next_node = node.next
        if next_node is not None:
            stack.append(next_node)


