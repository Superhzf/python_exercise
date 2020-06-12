# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flattenTree(self,root):
        if root is None:
            return None

        if root.left is None and root.right is None:
            return root

        leftTail = self.flattenTree(root.left)
        rightTail = self.flattenTree(root.right)

        if leftTail is not None:
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        return rightTail if rightTail is not None else leftTail
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenTree(root)

# leftTail is the The tail node of the flattened out left subtree
# What does the current node do?
# Assuming we have already transformed the left and the right halves of a given
# root node.The current node should put the left tail node point to the right tree
# and the right tree of the current node should be it's left tree.
