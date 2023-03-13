from requirements.ListNode import ListNode


def printNodeList(head: ListNode, end: str = ','):
    p = head
    while p is not None:
        print(p.val, end=end)
        p = p.next
