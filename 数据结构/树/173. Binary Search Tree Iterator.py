# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from requirements.TreeNode import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return []
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

        self.data = inorderTraversal(root)
        self.index = -1

    def next(self) -> int:
        self.index += 1
        return self.data[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.data)-1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
