# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from requirements.ListNode import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        counter = 0

        pointer = [p for _ in range(k)]

        while p is not None and counter < k:
            pointer[counter] = p
            p = p.next
            counter += 1

        if counter < k:
            return head

        pointer[0].next = self.reverseKGroup(head=pointer[-1].next, k=k)
        for i in range(k - 1, 0, -1):
            pointer[i].next = pointer[i - 1]

        return pointer[-1]
