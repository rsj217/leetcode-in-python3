

from src.datastruct.linknode import ListNode



nums = [1, 2,3, 2, 1]

head = ListNode.deserialize(nums)
print(head)

fast = head
slow = head
prev = None

while fast is not None and fast.next is not None:
    fast = fast.next.next
    next_ = slow.next
    slow.next = prev
    prev = slow
    slow = next_
    
print(slow)
print(prev)

