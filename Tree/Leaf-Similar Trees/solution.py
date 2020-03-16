# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder_iterate(self,root):
        current = root
        stack = []
        res = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                if current.left is None and current.right is None:
                    res.append(current.val)
                current = current.right
            else:
                break
        return res

    def leafSimilar(self,root1: TreeNode, root2: TreeNode) -> bool:
        leaf_seq1 = self.inorder_iterate(root1)
        leaf_seq2 = self.inorder_iterate(root2)
        return leaf_seq1 == leaf_seq2

# They key of this problem is that we MUST use DFS to traverse the tree
# BFS does not work!
