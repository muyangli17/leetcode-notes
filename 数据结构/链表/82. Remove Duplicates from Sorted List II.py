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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        placeHolder = ListNode(next=head)

        prev = placeHolder
        p = head
        q = p.next

        while p is not None:
            containDuplicate = False
            while q is not None and q.val == p.val:
                containDuplicate = True
                q = q.next

            if containDuplicate:
                prev.next = q
                p = q
            else:
                prev = prev.next
                p = p.next
            if q is not None:
                q = q.next

        return placeHolder.next


values = [1, 1, 2, 3, 3]
head = generateNodeList(values)

solution = Solution()
head = solution.deleteDuplicates(head=head)

printNodeList(head)
