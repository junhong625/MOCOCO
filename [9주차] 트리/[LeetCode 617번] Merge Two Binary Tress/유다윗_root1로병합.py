# 617. Merge Two Binary Trees
# 157ms / 15.6mb

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:                               # root1이 없을 경우 바로 root2 return
            return root2
        def preorder(n, k):                         
            if n and k:                             # n과 k 모두 존재할 경우,
                n.val += k.val                      # val 합산
                if n.left:                          # n의 왼쪽 자식이 있을 경우 왼쪽 자식으로 이동
                    preorder(n.left, k.left)
                elif k.left:                        # n.left는 없고 k.left만 있을 경우 n.left를 k.left로 지정(즉 k.left를 루트로 하는 서브트리 모두 가져옴)
                    n.left = k.left
                if n.right:                         # 왼쪽 자식노드 처리 과정과 동일
                    preorder(n.right, k.right)
                elif k.right:
                    n.right = k.right

        preorder(root1, root2)

        return root1