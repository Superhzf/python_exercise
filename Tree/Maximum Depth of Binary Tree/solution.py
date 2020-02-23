class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        else:
            len_l = self.maxDepth(root.left)
            len_r = self.maxDepth(root.right)
            if len_l > len_r:
                return len_l+1
            else:
                return len_r+1

# the idea is simple: calculate the length of left and right tree separately and
# add 1 for the root node
