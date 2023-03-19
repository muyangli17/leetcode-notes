from requirements.ListNode import ListNode
from requirements.TreeNode import TreeNode


def generateListNode(data: list) -> ListNode:
    p = ListNode(data[-1], None)
    for index in range(len(data) - 2, -1, -1):
        q = ListNode(val=data[index], next=p)
        p = q

    return p


def generateTree(datas: list):
    if len(datas) == 0:
        return None

    index = 0
    root = TreeNode(datas[index], None, None)
    index += 1
    nodeQueue = [root]

    while len(nodeQueue) > 0 and index < len(datas):
        latestNode = nodeQueue.pop(0)

        if datas[index] is not None:
            leftChild = TreeNode(datas[index], None, None)
            latestNode.left = leftChild
            nodeQueue.append(leftChild)
        index += 1

        if datas[index] is not None:
            rightChild = TreeNode(datas[index], None, None)
            latestNode.right = rightChild
            nodeQueue.append(rightChild)
        index += 1

    return root
