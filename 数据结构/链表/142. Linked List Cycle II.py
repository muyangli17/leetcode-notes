# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        nodes=[]
        while p is not None:
            if p not in nodes:
                nodes.append(p)
                p=p.next
            else:
                return p
        return None