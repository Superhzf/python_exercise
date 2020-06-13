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


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)

        for idx, value in enumerate(inorder):
            if value == root_val:
                inorder_left = inorder[:idx]
                inorder_right = inorder[idx+1:]

        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):-1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        return root
