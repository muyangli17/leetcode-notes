# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from requirements.TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        rootVal = preorder[0]
        rootIndex = inorder.index(rootVal)

        leftPreorder = preorder[1:rootIndex + 1]
        leftInorder = inorder[:rootIndex]

        rightPreorder = preorder[rootIndex + 1:]
        rightInorder = inorder[rootIndex + 1:]

        return TreeNode(rootVal,
                        self.buildTree(preorder=leftPreorder, inorder=leftInorder),
                        self.buildTree(preorder=rightPreorder, inorder=rightInorder))


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

solution = Solution()
T = solution.buildTree(preorder=preorder, inorder=inorder)


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)


print(preorderTraversal(T))
print(inorderTraversal(T))
