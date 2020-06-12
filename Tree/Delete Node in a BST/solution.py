# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                minNode = self.getMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root

    def getMin(self, root):
        while(root.left is not None):
            root = root.left
        return root

# What does the current node do?
# Checkout whether current node is equal to the key, if yes, then we have 3 situatios:
# 1. The current node does not have any children
# 2. The current node only has one child:
#   Put that child as the current node's successor
# 3. The current node has two children.
#   Find the min node of it's right tree, that value would be the new value
#   Delete that value from the right tree
