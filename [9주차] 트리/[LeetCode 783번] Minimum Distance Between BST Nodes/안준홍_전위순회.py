class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minV = 10 ** 5
        nodes = []
        def preorder(node):
            nodes.append(node.val)
            nonlocal minV
            if node.left:
                for i in nodes:
                    v = abs(i-node.left.val)
                    if 0 < v < minV:
                        minV = v
                preorder(node.left)
            if node.right:
                for i in nodes:
                    v = abs(i-node.right.val)
                    if 0 < v < minV:
                        minV = v
                preorder(node.right)
        preorder(root)
        return minV