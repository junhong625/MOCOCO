class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        root3 = TreeNode()
        def preorder(node1=root1, node2=root2, node3=root3):
            
            node3.val += 0 if not node1 else node1.val
            node3.val += 0 if not node2 else node2.val
            
            if (node1 and node1.left) or (node2 and node2.left):
                node3.left = TreeNode()
            if (node1 and node1.right) or (node2 and node2.right):
                node3.right = TreeNode()
            if node3.left:
                preorder(node1.left if node1 else [], node2.left if node2 else [], node3.left)
            if node3.right:
                preorder(node1.right if node1 else [], node2.right if node2 else [], node3.right)
                
        preorder()
        return root3