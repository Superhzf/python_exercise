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
# Use queue as the data structure
