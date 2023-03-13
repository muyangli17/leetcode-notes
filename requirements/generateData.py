from requirements.ListNode import ListNode
from requirements.TreeNode import TreeNode


def generateListNode(data: list) -> ListNode:
    p = ListNode(data[-1], None)
    for index in range(len(data) - 2, -1, -1):
        q = ListNode(val=data[index], next=p)
        p = q

    return p


def generateTree(datas: list):
    def insert(index):
        if datas[index] is not None:
            if (index + 1) * 2 < len(datas):
                return TreeNode(datas[index], insert((index + 1) * 2 - 1), insert((index + 1) * 2))
            elif (index + 1) * 2 - 1 < len(datas):
                return TreeNode(datas[index], insert((index + 1) * 2 - 1), None)
            else:
                return TreeNode(datas[index], None, None)
        else:
            return None

    return insert(0)
