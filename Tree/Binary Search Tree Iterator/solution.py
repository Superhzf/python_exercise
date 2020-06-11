# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.res = []
        stack = []
        curr = root
        while len(stack) > 0 or curr is not None:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            if len(stack) > 0:
                curr = stack.pop()
                self.res.append(curr.val)
                curr = curr.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.res.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.res) > 0

# This is actually an inorder traverse of a BST
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res = self.inorder(root)


    def inorder(self, root):
        res = []
        if root is not None:
            res = self.inorder(root.left)
            res.append(root.val)
            res = res + self.inorder(root.right)
        return res

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.res.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.res) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
