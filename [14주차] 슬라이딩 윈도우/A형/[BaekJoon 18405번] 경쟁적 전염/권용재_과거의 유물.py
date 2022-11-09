from collections import deque


N, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
S, X, Y = map(int,input().split())
delta = [(-1,0),(0,1),(1,0),(0,-1)]
virus = []
# 바이러스 찾기 (바이러스 크기도 포함)
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            virus.append((arr[i][j],i,j))
virus.sort()

dq = deque(virus)
time = 0
while dq:
    if time == S:
        break
    # 정렬을 했기 때문에 전체에 대한걸 돌리면 작은 값 부터채워짐
    for _ in range(len(dq)):
        size, x, y = dq.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y]
                    dq.append((arr[nx][ny], nx, ny))
    time += 1

print(arr[X-1][Y-1])