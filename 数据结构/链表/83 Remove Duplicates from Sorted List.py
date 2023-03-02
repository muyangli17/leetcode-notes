# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from requirements.ListNode import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = head
        p = prev.next

        while p is not None:
            if prev.val == p.val:
                prev.next = p.next
            else:
                prev = prev.next
            p = p.next

        return head


values = [1, 1, 2, 3, 3]

p = ListNode(values[-1], None)
for index in range(len(values) - 2, -1, -1):
    q = ListNode(val=values[index], next=p)
    p = q

head = p

solution = Solution()
head = solution.deleteDuplicates(head=head)

p = head
while p is not None:
    print(p.val)
    p = p.next
