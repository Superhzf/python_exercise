# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.res = []
        self.dfs(root, str(root.val))
        return self.res

    def dfs(self,root,path):
        if root.left is None and root.right is None:
            self.res.append(path)

        if root.left:
            self.dfs(root.left,path+"->"+str(root.left.val))

        if root.right:
            self.dfs(root.right,path+"->"+str(root.right.val))

# The idea is similar to Path Sum.
