# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List, Optional

from requirements.TreeNode import TreeNode
from requirements.generateData import generateTree


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        :param root:
        :return:
        """
        if root is None:
            return ""

        nextLayer = [root]
        res = ""

        while len(nextLayer) > 0:
            toVisit = nextLayer
            nextLayer = []

            while len(toVisit) > 0:
                p = toVisit.pop(0)
                if p is None:
                    res = res + 'N,'
                else:
                    res = res + str(p.val) + ','

                    nextLayer.append(p.left)
                    nextLayer.append(p.right)

        return res[:-1]

    def deserialize(self, data: str):
        """
        Decodes your encoded data to tree.
        :param data:
        :return:
        """
        data = data.split(',')
        if len(data) == 1:
            return None

        index = 0
        root = TreeNode(int(data[index]), None, None)
        index += 1
        nodeQueue = [root]

        while len(nodeQueue) > 0 and index < len(data):
            latestNode = nodeQueue.pop(0)

            if not data[index] == 'N':
                leftChild = TreeNode(int(data[index]), None, None)
                latestNode.left = leftChild
                nodeQueue.append(leftChild)
            index += 1

            if not data[index] == 'N':
                rightChild = TreeNode(int(data[index]), None, None)
                latestNode.right = rightChild
                nodeQueue.append(rightChild)
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

root = [1, 2, None]
root = generateTree(root)
solution = Codec()

ser = solution.serialize(root)
print(ser)

deser = solution.deserialize(ser)


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)


print(inorderTraversal(deser))
print(preorderTraversal(deser))
