# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        stack = [(root, [root.val])]
        num = 0

        while stack:
            node, totals = stack.pop()

            num += totals.count(total)

            if node.left:
                stack.append((node.left, [x+node.left.val for x in totals]+[node.left.val]))
            if node.right:
                stack.append((node.right, [x+node.right.val for x in totals]+[node.right.val]))
        return num
