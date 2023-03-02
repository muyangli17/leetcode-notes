# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from requirements.ListNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        res = None

        while head is not None:
            p = head
            head = head.next
            p.next = res
            res = p
        return res


values = [1, 2, 6, 3, 4, 5, 6]
val = 6

p = ListNode(values[-1], None)
for index in range(len(values) - 2, -1, -1):
    q = ListNode(val=values[index], next=p)
    p = q

head = p

solution = Solution()
head = solution.reverseList(head=head)

p = head
while p is not None:
    print(p.val)
    p = p.next
