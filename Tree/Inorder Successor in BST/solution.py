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

# The recursion version
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None:
            return
        if p.right is not None:
            res = p.right
            while res.left is not None:
                res = res.left
            return res

        self.p = p
        self.res = None
        self.inorder(root, False)
        return self.res

    def inorder(self, root, stop=False):
        tra = []
        if root is not None and not stop:
            tra = self.inorder(root.left, stop)
            if len(tra) > 0 and tra[-1] == self.p.val:
                self.res = root
                stop = True
            tra.append(root.val)
            tra += self.inorder(root.right, stop)
        return tra


# The easy but slow solution is traverse the tree using inorder style and find
# the node after p

# The second solution is that we traverse the tree in inorder style (iteratively),
# and at the same time write down the value of current node, if the previous node is
# what we want to delete, then return the current node
