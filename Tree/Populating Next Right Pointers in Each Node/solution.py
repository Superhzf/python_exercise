"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root

        values_by_level = [[root]]
        for this_level in values_by_level:
            next_level = []
            for node in this_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            if len(next_level) > 0:
                values_by_level.append(next_level)

        res = []
        for this_level in values_by_level:
            for index,node in enumerate(this_level):
                if index < len(this_level)-1:
                    node.next = this_level[index+1]
                else:
                    node.next = None
                res.append(node)

        return res[0]

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        self.out = []
        self.helper(root, 0)
        return self.out[0][0]


    def helper(self, root, height):
        if root is None:
            return None

        if len(self.out)<=height:
            self.out.append([])
        else:
            self.out[height][-1].next = root
        self.out[height].append(root)

        self.helper(root.left, height+1)
        self.helper(root.right, height+1)

# This is pretty much like the level order traversal.
# what does the current node do?
# Connect with it's previous node
