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

class Solution(object):
    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.total = total
        self.res = 0
        self.helper(root, True, self.total)
        return self.res

    def helper(self, root, start, target_sum):
        if root is None:
            return
        if root.val == target_sum:
            self.res += 1

        self.helper(root.left, False, target_sum-root.val)
        self.helper(root.right, False, target_sum-root.val)

        if start:
            self.helper(root.left, True, self.total)
            self.helper(root.right, True, self.total)

# What does the current node do?
# Checkout whether the value is equal to the target sum
# What does the helper function do?
# Check whether a sub tree can sum up to the target sum (no matter the target
# sum is the original required total or total - value of the current node)
