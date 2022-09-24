class Solution:
    def invertTree(self, root):
        def dfs(node=root):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            
            node.left, node.right = node.right, node.left
        dfs()
        return root