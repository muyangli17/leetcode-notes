# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from requirements.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        p = list1
        q = list2
        head = None

        if p.val < q.val:
            head = p
            p = p.next
        else:
            head = q
            q = q.next

        latestNode = head

        while p is not None and q is not None:
            if p.val < q.val:
                latestNode.next = p
                latestNode = latestNode.next
                p = p.next
            else:
                latestNode.next = q
                latestNode = latestNode.next
                q = q.next

        if p is None:
            latestNode.next = q
        if q is None:
            latestNode.next = p

        return head


value1 = [1, 2, 4]
value2 = [1, 3, 4]
n = 2

p = ListNode(value1[-1], None)
for index in range(len(value1) - 2, -1, -1):
    q = ListNode(val=value1[index], next=p)
    p = q

list1 = p

p = ListNode(value2[-1], None)
for index in range(len(value2) - 2, -1, -1):
    q = ListNode(val=value2[index], next=p)
    p = q

list2 = p

solution = Solution()
head = solution.mergeTwoLists(list1=list1, list2=list2)

p = head
while p is not None:
    print(p.val)
    p = p.next
