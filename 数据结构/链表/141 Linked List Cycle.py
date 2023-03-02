# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional

from requirements.ListNode import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        memAddr = []
        p = head
        while p is not None:
            if p in memAddr:
                return True
            else:
                memAddr.append(p)
            p=p.next
        return False
