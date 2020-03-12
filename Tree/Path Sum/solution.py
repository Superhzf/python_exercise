# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        else:
            if ((sum - root.val) == 0) and (root.left == None) and (root.right == None):
                return True
            if (root.left != None):
                if (self.hasPathSum(root.left,sum-root.val)):
                    return True
            if (root.right != None):
                if (self.hasPathSum(root.right,sum-root.val)):
                    return True
            return False
# the key here is to use sum-root.val
