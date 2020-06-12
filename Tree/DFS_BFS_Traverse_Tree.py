# https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/
from typing import List
class Node:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#    1
#    /\
#   2  3
#  /\
# 4  5

# BFS:
def BFS(root):
    queue = []
    queue.append(root)
    while(queue):
        temp = queue.pop(0) # We MUST use queue, stack does not work
        print (temp.val)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

res = []
def BFSRecur(queue: List[Node]) -> None:
    if len(queue) <= 0:
        return None
    curr = queue.pop(0)
    res.append(curr.val)
    if curr.left is not None:
        queue.append(curr.left)
    if curr.right is not None:
        queue.append(curr.right)
    # Repeat at the end of this level
    BFSRecur(queue)

# DFS: inorder: left, root, right
def inorder(root):
    res = []
    if root:
        res = inorder(root.left)
        res.append(root.val)
        res = res + inorder(root.right)
    return res

def inorderIter(root):
    stack = []
    curr = root
    res = []
    while len(stack) > 0 or curr is not None:

        while curr is not None:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


# DFS: preorder: root, left, right
def preorder(root):
    res = []
    if root:
        res.append(root.val)
        res = res+ preorder(root.left)
        res = res+ preorder(root.right)
    return res

def preorderTra(root):
    res = []
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    return res

# DFS: postorder: left, right, root
def postorder(root):
    res = []
    if root:
        res = res+ postorder(root.left)
        res = res+ postorder(root.right)
        res.append(root.val)
    return res

def postorder_iterative(root):
    res = []
    # Create two stacks
    s1 = []
    # Push root to first stack
    s1.append(root)

    # Run while first stack is not empty
    while s1:

        # Pop an item from s1 and
        # append it to s2
        node = s1.pop()
        s2.append(node)

        # Push left and right children of
        # removed item to s1
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
        # Print all elements of second stack
    return res[::-1]

# BFS vs DFS, when to use what?

# level order traversal:
class Solution:
    def LevelOrder(self, root):
        #inspired by the solution somewhat
        out = []
        def rec(node, height):
            if node:
                if len(out) <= height:
                    out.append([])
                out[height].append(node.val)
                rec(node.left, height + 1)
                rec(node.right, height + 1)
        rec(root, 0)
        return out
# this solution is very simple by adding a parameter height to let
# the function know which level the element should be.

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = []
        self.helper(root)
        return self.ans

    def helper(self, root):
        if root is None:
            return
        queue = [root]
        while(len(queue) > 0):
            curr_node = queue.pop(0)
            self.ans.append(curr_node.val)

            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)
