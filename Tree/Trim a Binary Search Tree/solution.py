
class Solution:
    def insert(self,root,key):
        current = root
        while True:
            if key < current.val and current.left is None:
                current.left = TreeNode(key)
                return
            elif key < current.val and current.left:
                current = current.left
            elif key > current.val and current.right is None:
                current.right = TreeNode(key)
                return
            elif key > current.val and current.right:
                current = current.right

    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        queue = [root]
        res = []
        while queue:
            current = queue.pop(0)
            if current.val >= L and current.val <= R:
                res.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        new_root = TreeNode(res[0])
        for node in res[1:]:
            self.insert(new_root,node)
        return new_root
# The solution above is straightforward by traversing the tree and finding out
# the available node. Then rebuild the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
            def trim(node):
                if node is None:
                    return None
                elif node.val > R:
                    return trim(node.left)
                elif node.val < L:
                    return trim(node.right)
                else:
                    node.left = trim(node.left)
                    node.right = trim(node.right)
                    return node
            return trim(root)
# The second solution is simpler using recursion
