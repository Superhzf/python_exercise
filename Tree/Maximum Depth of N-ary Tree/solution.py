"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0 #base case 1
        if not root.children:
            return 1 #base case 2
        heights = [] #hold all the heights of root's children
        for node in root.children:
            heights.append(self.maxDepth(node))
        return max(heights) + 1
