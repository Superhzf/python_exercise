# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        # To save the depth of the first node.
        self.recorded_depth = None
        self.is_cousin = False

    # defs returns True means either x or y is found, self.recorded_depth saves the
    # corresponding depth
    def dfs(self, node, depth, x, y):
        if node is None:
            return False

        # Don't go beyond the depth restricted by the first node found.
        if self.recorded_depth and depth > self.recorded_depth:
            return False

        # If true, it means that one of x or y is found.
        if node.val == x or node.val == y:
            if self.recorded_depth is None:
                # Save depth for the first node that is found (x or y)
                self.recorded_depth = depth
            # Return true, if the second node is found at the same depth.
            return self.recorded_depth == depth

        # left: either x or y is found in the left tree
        # right: either x or y is found in the right tree
        left = self.dfs(node.left, depth+1, x, y)
        right = self.dfs(node.right, depth+1, x, y)

        # self.recorded_depth != depth + 1 would ensure node x and y are not
        # immediate child nodes, otherwise they would become siblings.
        if left and right and self.recorded_depth != depth + 1:
            self.is_cousin = True

        return left or right

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        # Recurse the tree to find x and y
        self.dfs(root, 0, x, y)
        return self.is_cousin

# The idea is to find x and y and check whether they have the same parents
# What does the current node do?
# Checkout whether the current node is x or y. If both x and y is found and they
# are at the same depth, then checkout whether they are siblings, if not, set
# self.is_cousin to be True.
