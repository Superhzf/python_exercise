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

        ancestors = []

        while p is not None:
            ancestors.append(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q

# The idea is that
# Step 1: find the parent of all nodes at or above p and q
# Step 2: list all ancestors of p based on step 1
# Step 3: find ancestors of q one by one, if one of them shows up in step 2, then
# this is what we are looking for.

class Solution:

    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if current_node is None:
                return False

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)


            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans

# Recursion is an intuitive solution
# recurse_tree means whether p or q is found in the tree current_node
# 1. What does the current node should do?
# Confirm whether the current node is p or q
# 2. What does the left or right tree do?
# Find either p or q or both which has not been found
