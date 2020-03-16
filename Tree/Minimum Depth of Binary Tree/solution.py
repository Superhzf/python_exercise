# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if left_depth == 0:
            return right_depth + 1
        elif right_depth == 0:
            return left_depth + 1
        else:
            return min(left_depth,right_depth) + 1

# I solved this problem myself.
# The key is that when the right sub-tree or left sub-tree is none,
# it should return the length of the sub-tree of the other side.
