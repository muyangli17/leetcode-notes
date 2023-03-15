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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return []
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

        return inorderTraversal(root)[k - 1]


root = [1, 2, 3, 4, None, None, 5]
k = 2
root = generateTree(root)

solution = Solution()
print(solution.kthSmallest(root=root, k=k))
