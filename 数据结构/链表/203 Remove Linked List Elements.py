# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from requirements.ListNode import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next

        if head is None:
            return None

        prev = head
        p = prev.next

        while p is not None:
            if p.val == val:
                prev.next = p.next
            else:
                prev = p
            p = p.next
        return head


values = [1, 2, 6, 3, 4, 5, 6]
val = 6

p = ListNode(values[-1], None)
for index in range(len(values) - 2, -1, -1):
    q = ListNode(val=values[index], next=p)
    p = q

head = p

solution = Solution()
head = solution.removeElements(head=head, val=val)

p = head
while p is not None:
    print(p.val)
    p = p.next
