"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack = [root]
        res = []

        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack = stack + curr.children[::-1]

        return res
    
