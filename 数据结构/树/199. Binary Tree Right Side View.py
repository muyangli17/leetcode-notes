# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from requirements.TreeNode import TreeNode
from requirements.generateData import generateTree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nextLayer = [root]
        res = []

        while len(nextLayer) > 0:
            toVisit = nextLayer
            nextLayer = []
            valThisLayer = []

            for p in toVisit:
                if p is not None:
                    nextLayer.append(p.left)
                    nextLayer.append(p.right)
                    valThisLayer.append(p.val)

            if len(valThisLayer) > 0:
                res.append(valThisLayer[-1])

        return res


root = [1, 2, 3, None, 5, None, 4]
root = generateTree(root)

solution = Solution()
print(solution.rightSideView(root=root))
