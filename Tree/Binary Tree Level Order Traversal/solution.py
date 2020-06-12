# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return [[root.val]]
        value_by_level = [[root]]
        for this_level in value_by_level:
            next_level = []
            for node in this_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            if len(next_level) > 0:
                value_by_level.append(next_level)

        values = [[node.val for node in this_level] for this_level in value_by_level]
        return values

# This solution is so easy
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        self.out = []
        self.helper(root, 0)
        return self.out
    def helper(self, root, height):
        if root is None:
            return None

        if len(self.out) <= height:
            self.out.append([])

        self.out[height].append(root.val)
        self.helper(root.left, height+1)
        self.helper(root.right, height+1)
