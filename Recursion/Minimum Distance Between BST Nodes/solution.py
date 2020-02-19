class Solution:
    def minDiffInBST(self, root):

        queue = []
        l = []
        queue.append(root)
        l.append(root.val)

        while queue:
            node = queue.pop()
            if node.left:
                l.append(node.left.val)

                queue.append(node.left)
            if node.right:
                l.append(node.right.val)
                queue.append(node.right)
        minm = float("Inf")
        l.sort()
        for i in range(len(l)-1):
            if abs(l[i]-l[i+1]) < minm:
                minm = abs(l[i]-l[i+1])
        return minm

# The idea is simple, just traverse the tree and sort the values
