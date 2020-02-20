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
