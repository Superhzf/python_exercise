# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return None
		# define a queue for storing current level nodes, not all the nodes
        currentLevelNodes = [root]

		# result for saving
        result = []

        while len(currentLevelNodes) > 0:
			# put the current leve nodes into the result list
            result.append([node.val for node in currentLevelNodes])

			# print(result)

			# nextLevelNodes is a list for getting next level nodes
            nextLevelNodes = []
            for node in currentLevelNodes:
                if node.left is not None:
                    nextLevelNodes.append(node.left)
                if node.right is not None:
                    nextLevelNodes.append(node.right)

			# assgin nextLevelNodes to currentLevelNodes
            currentLevelNodes = nextLevelNodes

		# reverse the result for printing
        return result[::-1]

# Walk through the tree level by level

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        if root.left is None and root.right is None:
            return [[root.val]]
        self.out = []
        self.levelOrder(root, 0)
        return self.out[::-1]

    def levelOrder(self, root, height):
        if root is None:
            return
        if len(self.out) <= height:
            self.out.append([])
        self.out[height].append(root.val)
        self.levelOrder(root.left, height+1)
        self.levelOrder(root.right, height+1)
