# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        output = []
        self.inorder(root,output)
        l,r = 0 ,len(output) - 1
        while l < r:
            Sum = output[l] + output[r]
            if Sum == k:
                return True
            else:
                if Sum < k:
                    l += 1
                else:
                    r -= 1
        return False

    def inorder(self,root,output):
        if root == None:
            return
        else:
            self.inorder(root.left,output)
            output.append(root.val)
            self.inorder(root.right,output)

# The ieda is simple, traverse the tree in an inorder style and then find out
# in the list
