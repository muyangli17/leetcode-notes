# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from requirements.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return []
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

        T = inorderTraversal(root)

        if len(T) <= 1:
            return True

        for i in range(len(T) - 1):
            if T[i] >= T[i + 1]:
                return False
        return True
