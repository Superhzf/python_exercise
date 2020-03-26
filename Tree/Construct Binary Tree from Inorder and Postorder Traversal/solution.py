# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left=0,in_right=len(inorder)-1):
            if in_left > in_right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)
            index = inorder_map[root_val]


            # We MUST do the right subtree first because for postorder,
            # it does [left right root], when we do postorder.pop(), the right child
            # gets poped before the left one.
            root.right = helper(index+1,in_right)
            root.left = helper(in_left,index-1)

            return root


        inorder_map = {value:idx for idx,value in enumerate(inorder)}
        return helper()
