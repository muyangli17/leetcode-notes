# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from requirements.TreeNode import TreeNode
from requirements.generateData import generateTree


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        nextLayer = [root]
        positiveDirection = True
        res = []

        while len(nextLayer) > 0:
            toVisit = nextLayer
            nextLayer = []
            res.append([])

            while len(toVisit) > 0:
                p = toVisit.pop(0)
                res[-1].append(p.val)

                if positiveDirection:
                    if p.left is not None:
                        nextLayer.insert(0, p.left)
                    if p.right is not None:
                        nextLayer.insert(0, p.right)
                else:
                    if p.right is not None:
                        nextLayer.insert(0, p.right)
                    if p.left is not None:
                        nextLayer.insert(0, p.left)

            positiveDirection = not positiveDirection
        return res


root = [1, 2, 3, 4, None, None, 5]
root = generateTree(root)

solution = Solution()
print(solution.zigzagLevelOrder(root=root))
