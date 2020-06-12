# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.source = []
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return
        self.source = nums
        return self.helper(0,  len(nums) - 1)
    def helper(self, i, j):
        if i > j: return

        mid = (j + i) // 2
        node = TreeNode(self.source[mid])

        node.left = self.helper(i, mid - 1)
        node.right = self.helper(mid + 1, j)

        return node

# The idea is pretty much like a binary search

# The recursive version
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return
        size = len(nums)
        idx = int(size/2)
        root_val = nums[idx]
        root = TreeNode(root_val)
        root.left = self.sortedArrayToBST(nums[:idx])
        root.right = self.sortedArrayToBST(nums[idx+1:])
        return root

# What does the current node do?
# Find the root node and find out which part of nums belong to the left
# tree and which belongs to the right tree.
