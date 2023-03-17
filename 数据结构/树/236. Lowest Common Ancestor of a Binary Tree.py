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
        def containNode(root: TreeNode, target: int) -> bool:
            if root is None:
                return False
            if root.val == target:
                return True
            return containNode(root.left, target) or containNode(root.right, target)

        node = root

        while True:
            if containNode(node.left, p.val) and containNode(node.left, q.val):
                node = node.left
            elif containNode(node.right, p.val) and containNode(node.right, q.val):
                node = node.right
            else:
                return node


root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 4

root = generateTree(root)
p = TreeNode(p, None, None)
q = TreeNode(q, None, None)

solution = Solution()
print(solution.lowestCommonAncestor(root, p, q).val)
