# 297. Serialize and Deserialize Binary Tree
# 120ms / 20.2mb

from collections import deque
class Codec:
    def serialize(self, root):
        if not root:                                    # root가 None이면 바로 빈 문자열 출력
            return ''
        q = deque()                                     # queue
        root_s = f'{root.val}'                          # return값 / 초기값으로 root의 val 넣기
        q.append(root)                                  
        while q:                                        # q에 원소가 존재할 때까지 순회
            v = q.popleft()                             
            if v.left:                                  # v.left가 있으면 v.left의 val 값을 root_s에 넣어주고 q에 v.left 추가
                root_s += f' {v.left.val}'
                q.append(v.left)
            else:
                root_s += ' null'                       # v.left가 없으면 문자열 ' null' 추가
            if v.right:
                root_s += f' {v.right.val}'
                q.append(v.right)
            else:
                root_s += ' null'
                
        return root_s.rstrip(' null')                   # 오른쪽에 붙은 ' null'은 모두 제거
        

    def deserialize(self, data):
        if data == '':                                  # 빈 문자열을 받은 경우 return
            return
          
        root = deque(data.split())                      # root를 deque로
        for idx, d in enumerate(root):                  # root 순회하며 'null'은 None으로, 나머지는 정수로 형변환
            if d != 'null':
                root[idx] = int(d)
            else:
                root[idx] = None
        q = deque()                                     # queue
        head = TreeNode(root.popleft())                 # 트리의 루트를 head로 지정
        q.append(head)      
        while q:                                        # q에 원소가 있을 때까지 순회
            n = q.popleft()
            if root:                                    # root에 원소가 있을 경우,
                v = root.popleft()                      # 앞쪽 원소가 None이 아닐 경우 왼쪽 자식 노드로 지정해주고 q에 추가
                if v != None:
                    n.left = TreeNode(v)
                    q.append(n.left)
            if root:
                v = root.popleft()
                if v != None:
                    n.right = TreeNode(v)
                    q.append(n.right)      
        return head