# This script is about Binary Search Tree (BST)
class Node:
    def __init__(self,x):
        self.key = x
        self.left = None
        self.right = None

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)

#    8
#    /\
#   3  10
#  /\
# 1  6

# search
def search_BST(root,key):
    if root.key == key:
        return True
    if key > root.key and root.right is not None:
        return search_BST(root.right,key)
    if key < root.key and root.left is not None:
        return search_BST(root.left,key)
    return False

def search_BST_iterative(root,key):
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.key == key:
            return True
        elif key > current.key and current.right is not None:
            queue.append(current.right)
        elif key < current.key and current.left is not None:
            queue.append(current.left)
    return False
