# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        q = [root,root]

        while q:
            t1 = q.pop()
            t2 = q.pop()

            if t1 is None and t2 is None:
                continue

            if t1 is None or t2 is None:
                return False

            if t1.val!=t2.val:
                return False

            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)

        return True
