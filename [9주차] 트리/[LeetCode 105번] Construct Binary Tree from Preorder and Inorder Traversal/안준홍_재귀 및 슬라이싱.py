## 접근법
# 전위순회와 중위순회에서 찾을 수 있는 규칙을 찾다보니 전위순회에 대한 값들을 순서대로 기준을 잡고 본다면
# 해당 값을 기준으로 왼쪽에 속한 자식노드, 오른쪽에 속한 자식노드로 구분이 된다.
# 이를 활용하여 풀이


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:                                                     # inorder에 값이 존재할 경우만 시작
            parent = inorder.index(preorder.pop(0))                     # 부모 노드에 들어갈 값의 idx
            
            node = TreeNode(inorder[parent])                            # 부모 노드 설정
            node.left = self.buildTree(preorder, inorder[:parent])      # 왼쪽 자식노드
            node.right = self.buildTree(preorder, inorder[parent+1:])   # 오른쪽 자식노드
            return node                                                 # 생성한 트리 반환


