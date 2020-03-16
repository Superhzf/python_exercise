# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return [root.val]

        values_by_level = [[root]]
        for this_level in values_by_level:
            next_level = []
            for node in this_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            if len(next_level) > 0:
                values_by_level.append(next_level)

        values = [[node.val for node in this_level] for this_level in values_by_level]
        return [sum(value)/len(value) for value in values]
