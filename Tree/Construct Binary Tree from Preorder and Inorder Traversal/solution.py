# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left = 0, in_right = len(inorder)-1):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # build left subtree
            root.left = helper(in_left, index-1)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root

        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper()
