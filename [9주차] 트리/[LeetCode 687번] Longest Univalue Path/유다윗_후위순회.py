# 687. Longest Univalue Path
# 344ms / 18.1mb

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def postorder(n):                                                   # 후위순회 함수
            nonlocal max_len                                                # 최대 길이를 나타낼 변수
            
            if n:                                                           # 유효한 노드일 경우,
                left_sum_len, left_val = postorder(n.left)                  # 왼쪽 서브트리 순회 -> 길이 누적값과 왼쪽 자식의 val 받기
                right_sum_len, right_val = postorder(n.right)               # 오른쪽 서브트리 순회 -> 길이 누적값과 오른쪽 자식의 val 받기
                
                if left_val == right_val == n.val:                          # 자식 노드들의 val과 현재 노드 val 모두 일치할 경우,
                    now_len_sum = left_sum_len + right_sum_len + 2          # 왼쪽서브트리-현재-오른쪽서브트리 연결 길이 구하기
                    if now_len_sum > max_len:                               # 최대 길이 갱신
                        max_len = now_len_sum
                        
                now_len_sum = 0                                             # 위에서 계산한 now_len_sum은 retunrn 값으로 쓰이면 안 되기 때문에 초기화
                if left_val == n.val:                                       # 왼쪽 자식 노드 val과 현재 노드 val이 일치할 경우
                    now_len_sum = left_sum_len + 1
                if right_val == n.val:                                      # 오른쪽 자식 노드 val과 현재 노드 val이 일치할 경우
                    now_len_sum = max(right_sum_len + 1, now_len_sum)
                
                if now_len_sum > max_len:                                   # 최대 길이 갱신
                    max_len = now_len_sum
                
                return now_len_sum, n.val
            
            else:                                                           # 유효하지 않은 노드일 경우,
                return 0, None
    
    
        max_len = 0
        postorder(root)

        return max_len