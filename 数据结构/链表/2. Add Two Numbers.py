# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from requirements.ListNode import ListNode
from requirements.generateData import generateNodeList
from requirements.printData import printNodeList


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        p.val += q.val
        p = p.next
        q = q.next

        prev = l1

        while p is not None and q is not None:
            p.val += q.val
            p = p.next
            q = q.next
            prev = prev.next

        if p is None:
            prev.next = q

        p = l1
        up = p.val >= 10
        p.val = p.val % 10
        p = p.next

        prev = l1

        while p is not None:
            p.val += 1 * up
            up = p.val >= 10
            p.val = p.val % 10
            p = p.next
            prev = prev.next

        if up:
            one = ListNode(val=1, next=None)
            prev.next = one

        return l1


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

l1 = generateNodeList(l1)
l2 = generateNodeList(l2)

solution = Solution()
head = solution.addTwoNumbers(l1=l1, l2=l2)

printNodeList(head)
