# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from requirements.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        for i in range(n):
            p = p.next

        if p is None:
            return head.next

        q = head

        while p.next is not None:
            p = p.next
            q = q.next

        q.next = q.next.next

        return head


values = [1, 2, 3, 4, 5, 6]
n = 2

p = ListNode(values[-1], None)
for index in range(len(values) - 2, -1, -1):
    q = ListNode(val=values[index], next=p)
    p = q

head = p

solution = Solution()
head = solution.removeNthFromEnd(head=head, n=n)

p = head
while p is not None:
    print(p.val)
    p = p.next
