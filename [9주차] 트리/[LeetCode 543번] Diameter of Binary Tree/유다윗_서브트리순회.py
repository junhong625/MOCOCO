# 543. Diameter of Binary Tree
# 479ms / 17mb

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        subtree_depth = 1                               # subtree의 최대 깊이를 나타낼 변수
        def postorder(n, depth):                        # subtree를 순회하는 후위순회 함수
            nonlocal subtree_depth

            if n:
                postorder(n.left, depth+1)
                postorder(n.right, depth+1)
                if depth > subtree_depth:               # 현재 노드에서의 깊이가 subtree_depth보다 더 깊을 경우 값 갱신
                    subtree_depth = depth

        def preorder(n):                                # 루트를 이동시킬 전위순회 함수
            nonlocal max_length                         # return값(input 트리의 노드 to 노드 최대 길이)
            nonlocal subtree_depth

            now_depth = 0                               # 현재 루트에서의 노드 to 노드 최대 길이
            if n:                                       # 유효한 노드일 경우,
                left_root = n.left
                right_root = n.right
                
                if left_root:                           # 왼쪽 서브트리
                    subtree_depth = 1                   # subtree_depth 초기화
                    postorder(left_root, 1)
                    now_depth += subtree_depth
               
                if right_root:                          # 오른쪽 서브트리
                    subtree_depth = 1
                    postorder(right_root, 1)
                    now_depth += subtree_depth
                
                if now_depth > max_length:              # 현재 루트에서의 노드 to 노드 최대 길이가 max_length보다 길 경우 값 갱신
                    max_length = now_depth
                
                preorder(n.left)                        # 왼쪽 자식 노드로 이동
                preorder(n.right)                       # 오른쪽 자식 노드로 이동


        max_length = 0
        preorder(root)

        return max_length