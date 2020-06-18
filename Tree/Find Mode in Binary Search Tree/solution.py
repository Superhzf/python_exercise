# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    prev = None
    max_count = 0
    current_count = 0
    result = []

    def findMode(self, root):
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        self.current_count = 1 if node.val != self.prev else self.current_count + 1
        if self.current_count == self.max_count:
            self.result.append(node.val)
        elif self.current_count > self.max_count:
            self.result = [node.val]
            self.max_count = self.current_count
        self.prev = node.val
        self.dfs(node.right)

# The key to this solution is that the space complexity is O(1)
# The idea is that using INORDER TRAVEL, so result would be sorted.

# Solution 2
# It is more intuitive but it cannot pass all test cases, I don't know why
# please try yourself for more details.
class Solution(object):
    prev = None
    res = []
    curr_count = 0
    max_count = 0
    def findMode(self, root):
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return None
        if self.prev is None:
            self.prev = root.val
            self.curr_count = 1
            self.max_count = 1
        else:
            if root.val == self.prev:
                self.curr_count += 1
            else:
                self.curr_count = 1

        if self.curr_count == self.max_count:
            self.res.append(root.val)
        elif self.curr_count > self.max_count:
            self.res = [root.val]
            self.max_count = self.curr_count
        self.prev = root.val
        self.dfs(root.left)
        self.dfs(root.right)
