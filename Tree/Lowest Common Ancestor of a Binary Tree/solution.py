# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root:None}

        while p not in parent or q not in parent:
            curr = stack.pop()
            if curr.left is not None:
                parent[curr.left] = curr
                stack.append(curr.left)
            if curr.right is not None:
                parent[curr.right] = curr
                stack.append(curr.right)

        ancestors = set()

        while p is not None:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q

# The idea is that
# Step 1: find the parent of all nodes at or above p and q
# Step 2: list all ancestors of p based on step 1
# Step 3: find ancestors of q one by one, if one of them shows up in step 2, then
# this is what we are looking for.
