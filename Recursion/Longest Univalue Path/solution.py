# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if node is None:
                return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = 0
            right_arrow = 0
            if node.left is not None and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right is not None and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans

# The key here is that we have to add the length of left and right, not just one side
