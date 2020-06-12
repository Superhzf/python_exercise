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

# my solution which is easier to understand but slower.
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])

        for idx, ele in enumerate(inorder):
            if ele == root.val:
                left_tree_in = inorder[:idx]
                right_tree_in = inorder[idx+1:]
                break

        left_tree_pre = preorder[1:len(left_tree_in)+1]
        right_tree_pre = preorder[len(left_tree_in)+1:]

        root.left = self.buildTree(left_tree_pre, left_tree_in)
        root.right = self.buildTree(right_tree_pre, right_tree_in)
        return root

# 1.What does the current node do?
# Find the root node and the preorder and inorder for the left and right sub-trees
