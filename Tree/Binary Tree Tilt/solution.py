# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0
        self.tilt = 0
        self.getSum(root)
        return self.tilt

    def getSum(self, root):
        if root is None:
            return 0
        left = self.getSum(root.left)
        right = self.getSum(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val
# What does the current node do?
# Calculate the sum of it's left tree and right tree. At the same time, tilt is
# calculated
