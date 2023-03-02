# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from requirements.TreeNode import TreeNode
from requirements.generateData import generateTree


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p = 2
q = 4
root = generateTree(root)
p = TreeNode(p, None, None)
q = TreeNode(q, None, None)

solution = Solution()
print(solution.lowestCommonAncestor(root, p, q).val)
