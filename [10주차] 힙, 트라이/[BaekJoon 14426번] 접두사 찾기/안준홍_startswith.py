import sys

N, M = map(int, sys.stdin.readline().strip().split())

temp = []                                       # 문자열 집합
for i in range(N):
    temp.append(sys.stdin.readline().strip())

find = []                                       # 접두사인지 확인할 문자열
for i in range(M):
    find.append(sys.stdin.readline().strip())

temp.sort()                                     # 두 리스트 모두 정렬 
find.sort()


cnt = 0
idx = 0

for i in find:                                  
    for j in range(idx, N):                     # 같은 문자열이 여러번 주어지는 경우가 없고 정렬을 했기 때문에 탐색의 기준점을 idx로 지정해도 무방
        if temp[j].startswith(i):               # temp[j]의 문자열이 i로 시작하는지 판단
            cnt += 1                            # 접두사일 경우 cnt + 1
            idx = j                             # idx 변경
            break

print(cnt)
