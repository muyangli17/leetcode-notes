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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        if targetSum == root.val and root.left is None and root.right is None:
            return [[root.val]]

        ans = []
        for _ in self.pathSum(root.left, targetSum - root.val) + self.pathSum(root.right, targetSum - root.val):
            ans.append([root.val] + _)
        return ans


root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
targetSum = 22
root = generateTree(root)

solution = Solution()
print(solution.pathSum(root=root, targetSum=targetSum))
