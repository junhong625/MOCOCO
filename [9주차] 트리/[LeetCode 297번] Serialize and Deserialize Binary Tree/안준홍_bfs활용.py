from collections import deque

class Codec:
    def serialize(self, root):
        if root:                            # root가 존재할 경우에만 진행
            ser_list = str(root.val) + ' '  # 시작점에 대한 값을 직렬화한 문자에 추가
            def bfs(node = root):           # bfs 정의
                nonlocal ser_list           # 직렬화 호출
                q = deque([node])           # q에 현재 node추가
                while q:                    # q가 존재하지 않을 때 까지 반복
                    for _ in range(len(q)): # 같은 레벨의 노드들이 출력될 수 있도록 반복
                        node = q.popleft()  # q에 들어있는 가장 첫번째 노드를 빼내서 node에 저장 
                                            # 직렬화에 해당 노드의 왼쪽, 오른쪽 자식 노드 존재여부에 따라 문자 추가
                        ser_list += str(node.left.val) + ' ' if node.left else 'null' + ' '
                        ser_list += str(node.right.val) + ' ' if node.right else 'null' + ' '
                        
                        if node.left:       # 왼쪽 자식 노드가 존재할 경우에 q에 추가
                            q.append(node.left)
                        if node.right:      # 오른쪽 자식 노드가 존재할 경우에 q에 추가
                            q.append(node.right)
            bfs()                           # bfs(탐색 시작)
            return ser_list.rstrip('null ') # 오른쪽에 들어있는 null문자열 모두 제거

        return ''                           # 입력값이 없을 경우    
                
    def deserialize(self, data):
        if not data:                        # 입력값이 없을 경우
            return
        data = deque(data.split(' '))       # 입력값을 분해해서 deque 자료형으로 data에 저장
        root = TreeNode(data.popleft())     # 제일 처음 값을 루트 노드로 설정 
        q = deque([root])                   # q에 루트 노드 저장
        while data and q:                   # data와 q가 존재할 때만 진행
            v = q.popleft()                 # q에서 가장 첫번째 노드 추출 
            if data:                        # data가 존재할 경우 왼쪽 자식 노드에 data의 가장 앞에 있는 값을 꺼내서 저장 후
                v.left = TreeNode(data.popleft())
                q.append(v.left)            # 왼쪽 자식 노드를 q에 추가
            if data:                        # data가 존재할 경우 오른쪽 자식 노드에 data의 가장 앞에 있는 값을 꺼내서 저장 후
                v.right = TreeNode(data.popleft())
                q.append(v.right)           # 오른쪽 자식 노드를 q에 추가
        return root                         # 생성한 트리노드 반환