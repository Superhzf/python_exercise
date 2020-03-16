# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return []

        values_by_level = [[root]]
        for this_level in values_by_level:
            next_level = []
            for c in this_level:
                if c.left:
                    next_level.append(c.left)
                if c.right:
                    next_level.append(c.right)
            if len(next_level)>0:
                values_by_level.append(next_level)

        values = [[x.val for x in z ] for z in values_by_level]
        return [sum(v) / float(len(v)) for v in values]
