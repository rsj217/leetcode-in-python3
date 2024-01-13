from typing import List

from src.datastruct.linknode import ListNode

arr = [0, 1, 2, 3, 4, 5, 6]

root = ListNode.deserialize(arr)

print(root)


def reverser(root):
    prev = None
    node = root
    
    while node is not None:
        next_ = node.next
        node.next = prev
        prev = node
        node = next_
    
    return prev




ans = reverser(root)
print("ans", ans)
