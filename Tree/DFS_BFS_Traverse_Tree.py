class Node:
    def __init__(self,x):
        self.key = x
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
        temp = queue.pop(0)
        print (temp.key)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
# DFS: inorder
def inorder(root):
    res = []
    if root:
        res = inorder(root.left)
        res.append(root.key)
        res = res + inorder(root.right)
    return res

# DFS: preorder
def preorder(root):
    res = []
    if root:
        res.append(root.key)
        res = res+ preorder(root.left)
        res = res+ preorder(root.right)
    return res

# DFS: postorder
def postorder(root):
    res = []
    if root:
        res = res+ postorder(root.left)
        res = res+ postorder(root.right)
        res.append(root.key)
    return res
