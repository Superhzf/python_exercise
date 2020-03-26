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
