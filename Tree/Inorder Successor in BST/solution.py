# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # If the right subtree is not None, the successor is in there
        if p.right is not None:
            p = p.right
            while p.left is not None:
                p = p.left
            return p

        stack = []
        pre_value = float('-inf')

        # If the right subtree is None, then the successor node is somewhere upper p
        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pre_value == p.val:
                return root
            pre_value = root.val
            root = root.right

        return None

# The easy but slow solution is traverse the tree using inorder style and find
# the node after p

# The second solution is that we traverse the tree in inorder style (iteratively),
# and at the same time write down the value of current node, if the next node is
# what we want to delete, then return the current node
