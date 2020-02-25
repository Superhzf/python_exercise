# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def BFS(self,root):
        if root is None:
            return 0
        queue = [root]
        total_sum = 0
        while queue:
            current = queue.pop(0)
            total_sum += current.val

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return total_sum

    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0

        res = []
        queue = [root]

        while queue:
            current = queue.pop(0)
            curr_l = self.BFS(current.left)
            curr_r = self.BFS(current.right)
            res.append(abs(curr_l-curr_r))
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return sum(res)

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tilt, total = self.__findTilt(root)
        return tilt

    def __findTilt(self, root: TreeNode) -> int:
        """
        what's LEFT tilt, total sum?
        what's RIGHT tilt, total sum?
        tilt |L - R|
        return tilt + L_til + R_til
        """

        if root is None:
            return 0, 0
        L_tilt, L_total = self.__findTilt(root.left)
        R_tilt, R_total = self.__findTilt(root.right)
        tilt = abs(L_total - R_total)
        return tilt + L_tilt + R_tilt, root.val + L_total + R_total
# The base solution is iterate each node and calculate it's left tilt and right
# tilt, finally, add them up, it is only faster than 8% of Python submissions
