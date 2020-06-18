# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0

        res = []

        stack = [root]

        while stack:
            curr = stack.pop()
            if curr.left is None and curr.right is None:
                res.append(curr.val)
                continue

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                if curr.right.left is not None or curr.right.right is not None:
                    stack.append(curr.right)

        return sum(res)

# recursion version
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        leftsum = self.helper(root, False)
        return leftsum

    def helper(self, root, isLeft):
        if root is None:
            return 0
        elif root.left is None and root.right is None and isLeft:
            return root.val
        elif root.left is None and root.right is None and not isLeft:
            return 0
        left = self.helper(root.left, True)
        right = self.helper(root.right, False)
        return left + right
