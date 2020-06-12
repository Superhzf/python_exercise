# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This is hard to understand
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return [[root.val]]

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
        i = 1
        while i < len(values):
            values[i] = values[i][::-1]
            i += 2
        return values


class Solution:
    def zigzagLevelOrder(self, root):
        out = []
        def helper(root, height):
            if root is None:
                return
            if len(out) <= height:
                out.append([])
            out[height].append(root.val)
            helper(root.left, height+1)
            helper(root.right, height+1)

        helper(root,0)
        return [out[i] if i%2==0 else out[i][::-1] for i in range(len(out))]
# This solution is very nice by using a parameter height to
# let the function know which level the element should be
# What does the current node do?
# Put the node into the right level
