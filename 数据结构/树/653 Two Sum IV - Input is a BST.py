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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return []
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

        T = inorderTraversal(root)

        i = 0
        j = len(T) - 1

        while i < j:
            if T[i] + T[j] == k:
                return True
            elif T[i] + T[j] > k:
                j -= 1
            else:
                i += 1

        return False


root = [5, 3, 6, 2, 4, None, 7]
root = generateTree(root)
k = 9

solution = Solution()
print(solution.findTarget(root, k))
