# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self,root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height,right_height)+1

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return abs(right_height-left_height)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# They key here is that all the subtrees
# should be balanced too, not just subtrees of the root node
