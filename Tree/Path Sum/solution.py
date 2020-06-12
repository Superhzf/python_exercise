# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == target:
            return True

        if self.hasPathSum(root.left, target - root.val):
            return True
        if self.hasPathSum(root.right, target - root.val):
            return True

# What does the current node do?
# Checkout whether current node value is equal to the target
