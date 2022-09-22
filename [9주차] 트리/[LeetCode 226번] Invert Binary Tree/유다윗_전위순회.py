# 226. Invert Binary Tree
# 61ms / 13.7mb

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def preorder(n):                                # 전위함수 정의
            if n:
                n.left, n.right = n.right, n.left       # 자식노드 위치 교환
                preorder(n.left)
                preorder(n.right)
        
        preorder(root)

        return root