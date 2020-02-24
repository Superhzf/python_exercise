# solution 1
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return None
        stack=[root]
        nodes=[]
        while stack:
            node=stack.pop()
            nodes.append(node.val)
            if not node.left and not node.right:
                continue
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        if len(set(nodes))!=len(nodes):
               return 0
        nodes.sort()
        dis=[]
        for i in range(len(nodes)-1):
            dis.append(abs(nodes[i]-nodes[i+1]))
        return min(dis)
# This is boring, the idea is that traverse all nodes, sort the nodes and find the
# minimum difference

# Solution 2
class Solution(object):
    def getMinimumDifference(self, root):
        def fn(node, lo, hi):
            if not node: return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)
        return fn(root, float('-inf'), float('inf'))

# Keep track of the lo and hi bounds of each node,
# when you've passed the leaf nodes, compute hi - lo
# to get the lowest difference along that path
