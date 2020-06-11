# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTHelp(root, None, None)

    def isValidBSTHelp(self, root: TreeNode, min_node: TreeNode, max_node: TreeNode):
        if root is None:
            return True

        if min_node is not None and root.val <= min_node.val:
            return False

        if max_node is not None and root.val >= max_node.val:
            return False

        return self.isValidBSTHelp(root.left, min_node, root) & self.isValidBSTHelp(root.right, root, max_node)

# What does the curr_node should do?
# Compare whether it is less than the left sub-tee and larger than the right
# sub-tree
# What does the recursion function do?
# checkout whether the left sub-tree and the right sub-tree are valid
