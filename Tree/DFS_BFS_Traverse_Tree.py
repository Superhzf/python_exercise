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
        temp = queue.pop(0) # We MUST use queue, stack does not work
        print (temp.key)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

# DFS: inorder: left, root, right
def inorder(root):
    res = []
    if root:
        res = inorder(root.left)
        res.append(root.key)
        res = res + inorder(root.right)
    return res

def inorder_iterate(root):
    current = root
    stack = []
    res = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            res.append(current.key)
            current = current.right
        else:
            break
    return res

# DFS: preorder: root, left, right
def preorder(root):
    res = []
    if root:
        res.append(root.key)
        res = res+ preorder(root.left)
        res = res+ preorder(root.right)
    return res

def preorder_iterate(root):
    queue = [root]
    res = []
    while queue:
        current = queue.pop(0)
        res.append(current.key)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return res

# DFS: postorder: left, right, root
def postorder(root):
    res = []
    if root:
        res = res+ postorder(root.left)
        res = res+ postorder(root.right)
        res.append(root.key)
    return res

def postorder_iterative(root):

    res = []
    # Create two stacks
    s1 = []
    s2 = []

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
    while s2:
        node = s2.pop()
        res.append(node.key)
    return res

# BFS vs DFS, when to use what?
