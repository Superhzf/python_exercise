# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""

        # None of left or right child exists
        if t.left is None and t.right is None:
            return str(t.val)

        # Only the left child exists
        if t.right is None:
            return str(t.val)+"("+self.tree2str(t.left)+")"

        # both left and right child exists as well as only the right child exists but we still need the braces
        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"

# This problem is handled based on different cases
# case1: None of left or right child exists
# case2: Only the left child exists
# case3: Only the right child exists
# case4: Both left and right child exists
# case3 and case 4 can be handled together because we still need braces for case3
