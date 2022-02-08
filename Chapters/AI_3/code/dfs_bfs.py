### Model (binary tree)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### Algorithms
class BinaryTreeUtils:
    def dfs(self, root: TreeNode) -> [int]:
        tree_values = []
        
        def preOrder(root):
            if root:
                tree_values.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
            
            return tree_values
            
        return preOrder(root)
        
    def bfs(self, root: TreeNode) -> [int]:
        tree_values = []
        
        def levelOrder(root):
            if not root:
                return []
            
            queue = []
            queue.append(root)
            
            while queue:
                curr = queue.pop(0)
                tree_values.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            
            return tree_values
            
        return levelOrder(root)
        
### Main
# Binary tree:
#         1
#      /    \
#     2     3
#    / \   / \
#   4  5  6  7
root = TreeNode(1)
lnode = TreeNode(2)
rnode = TreeNode(3)
root.left = lnode
root.right = rnode
lnode.left = TreeNode(4)
lnode.right = TreeNode(5)
rnode.left = TreeNode(6)
rnode.right = TreeNode(7)

# algorithms
utils = BinaryTreeUtils()

# dfs
dfs_values = utils.dfs(root)
print(f"DFS: {*dfs_values,}")

# bfs
bfs_values = utils.bfs(root)
print(f"BFS: {*bfs_values,}")

