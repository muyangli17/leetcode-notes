# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from requirements.TreeNode import TreeNode


class Solution:
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        # “中序遍历序列回文”是必要但不充分条件
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return []
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

        T = inorderTraversal(root)

        stack = []
        for i in range(len(T) // 2):
            stack.append(T[i])

        for i in range(len(T) // 2 + 1, len(T)):
            if stack.pop() != T[i]:
                return False
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetricSubTree(p: TreeNode, q: TreeNode) -> bool:
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return isSymmetricSubTree(p.left, q.right) and isSymmetricSubTree(p.right, q.left)

        return isSymmetricSubTree(root.left, root.right)
