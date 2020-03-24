# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def successor(self,root):
        root = root.right
        while root.left is not None:
            root = root.left
        return root.val

    def predecessor(self,root):
        root = root.left
        while root.right is not None:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.right is not None:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right,root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left,root.val)

        return root

# The solution to problem should take the advantage of BST
# The successor after deleting the key value is the smallest value that is larger
# than it
# The predecessor after deleting the key value is the largest value that is smaller
# than it
# The reason to think about successor and predecessor is that if the right sub-tree
# is not none, we adjust the right sub-tree which uses successor, otherwise, we
# use predecessor
