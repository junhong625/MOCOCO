class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        if not root or (not root.left and not root.right): # root가 없거나 양쪽 노드가 존재하지 않을 경우 바로 0을 반환하며 종료
            return 0
        
        ## dfs 탐색으로 각 노드 마다의 최대 노드 수 탐색
        def dfs(node=root):             # root를 무조건 시작점으로 지정
            if not node:                # 해당 노드에 값이 없을 경우 0을 반환
                return 0    
            left = dfs(node.left)       # 왼쪽 노드 탐색
            right = dfs(node.right)     # 오른쪽 노드 탐색
            
            nonlocal total              # enclose scope에 있는 total 호출
            if left+right > total:      # 왼쪽 노드 수와 오른쪽 노드 수의 합을 더합 값이 total보다 클 경우 
                total = left+right      # total의 값을 왼쪽 노드 수와 오른쪽 노드 수의 합으로 변경
            return 1 + left if left > right else 1 + right  # 각 dfs마다 왼쪽 노드와 오른쪽 노드 중 더 깊은 곳으로 탐색한 값을 반환
        
        total = 0
        dfs()
        return total