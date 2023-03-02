# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from requirements.TreeNode import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val, None, None)

        p = root

        while p is not None:
            if val < p.val:
                if p.left is None:
                    temp=TreeNode(val, None,None)
                    p.left=temp
                    break
                else:
                    p = p.left
            else:
                if p.right is None:
                    temp=TreeNode(val, None,None)
                    p.right=temp
                    break
                else:
                    p = p.right

        return root
