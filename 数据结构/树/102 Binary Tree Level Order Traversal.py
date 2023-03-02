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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        L = self.levelOrder(root.left)
        R = self.levelOrder(root.right)

        i = 0
        j = 0
        res = []
        while i < len(L) and j < len(R):
            res.append(L[i] + R[j])
            i += 1
            j += 1

        if i < len(L):
            for k in range(i, len(L)):
                res.append(L[k])

        if j < len(R):
            for k in range(j, len(R)):
                res.append(R[k])
        return [[root.val]] + res


root = [5, 3, 6, 2, 4, None, 7]
root = generateTree(root)
k = 9

solution = Solution()
print(solution.levelOrder(root))
