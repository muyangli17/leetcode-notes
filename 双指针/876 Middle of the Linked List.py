# Definition for singly-linked list.
# requirements ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
from typing import Optional

from requirements.ListNode import ListNode


class Solution:
    def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        length = 0
        while p != None:
            length += 1
            p = p.next

        p = head
        for i in range(math.floor(length / 2)):
            p = p.next

        return p

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = pp = head
        while not pp is None:
            pp = pp.next
            if pp is None:
                return p
            else:
                pp = pp.next
            p = p.next
        return p


values = [1, 2, 3, 4, 5, 6]
p = ListNode(values[-1], None)
for index in range(len(values) - 2, -1, -1):
    q = ListNode(val=values[index], next=p)
    p = q

head = p

solution = Solution()
mid = solution.middleNode(head=head)
while mid is not None:
    print(mid.val)
    mid = mid.next
