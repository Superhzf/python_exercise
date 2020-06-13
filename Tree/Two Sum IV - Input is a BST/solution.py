# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        stack = [root]
        traverse = set()
        while stack:
            curr = stack.pop()
            if k-curr.val in traverse:
                return True
            else:
                traverse.add(curr.val)

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return False
