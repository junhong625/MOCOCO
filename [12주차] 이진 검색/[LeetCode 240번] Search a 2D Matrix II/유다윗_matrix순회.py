# 240. Search a 2D Matrix II
# 221ms / 20.4mb

# flow
# 1. 현재 행에서 오른쪽으로 이동하며 target 이하이면서 가장 큰 숫자 찾기
# 2. 해당 숫자에서 아래로 내려가며 target 찾기
# 3. 못 찾으면 다음 행으로 이동해서 위 과정 반복

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.M = len(matrix)
        self.N = len(matrix[0])
        
        row = 0
        col_limit = self.N - 1                                      # 이미 탐색했던 칼럼의 인덱스 중 최소
        while row < self.M:
            col = 0
            while col < col_limit and matrix[row][col] < target :   # col 오른쪽으로 이동
                col += 1
            if matrix[row][col] == target:                          # target을 찾았으면 True return
                return True
            elif matrix[row][col] > target:                         # target보다 큰 값 조건으로 위 while문을 탈출했을 경우 col -1 
                col -= 1    
            if col == col_limit:                                    # 이미 탐색했던 칼럼일 경우 다음 행 순회
                row += 1
                continue

            col_limit = col                                         # col_limit 업데이트

            temp_row = row                                          # temp_row: 현재 칼럼의 행 순회
            while temp_row < self.M:
                if matrix[temp_row][col] == target:
                    return True
                temp_row += 1
            row += 1
        return False                                                # 탐색 실패



############## bfs 접근은 시간초과 (124 / 129)###################
from collections import deque
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.M = len(matrix)
        self.N = len(matrix[0])
        delta = [[0, 1], [1, 0]]
        def bfs():
            visited = [[0] * self.N for _ in range(self.M)]
            q = deque()
            q.append([0, 0])
            while q:
                now = q.popleft()
                visited[now[0]][now[1]] = 1
                if matrix[now[0]][now[1]] == target:
                    return True
                elif matrix[now[0]][now[1]] < target:
                    for d in delta:
                        next_row = now[0] + d[0]
                        next_col = now[1] + d[1]
                        if next_row < self.M and next_col < self.N and not visited[next_row][next_col]:
                            q.append([next_row, next_col])
            return False

        return bfs()