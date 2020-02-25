# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False

        q = deque([s])
        while len(q):
            node = q.popleft()
            if node.val == t.val:
                if self.isSame(node, t):
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False

    def isSame(self, t, k):
        if not t and not k:
            return True
        elif not t or not k:
            return False
        elif t.val != k.val:
            return False
        else:
            return self.isSame(t.left, k.left) and self.isSame(t.right, k.right)

# Note that s and t are regular binary tree instead of BST
# Straight forward, just find the node in s and then test whether the subtree starting
# from that point is different from t
