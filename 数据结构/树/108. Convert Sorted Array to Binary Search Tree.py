# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from requirements.TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(val=nums[0], left=None, right=None)
        return TreeNode(val=nums[len(nums) // 2],
                        left=self.sortedArrayToBST(nums[:len(nums) // 2]),
                        right=self.sortedArrayToBST(nums[len(nums) // 2 + 1:]))


nums = [1, 2, 3, 4, 5]

solution = Solution()
T = solution.sortedArrayToBST(nums=nums)


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


print(inorderTraversal(T))
