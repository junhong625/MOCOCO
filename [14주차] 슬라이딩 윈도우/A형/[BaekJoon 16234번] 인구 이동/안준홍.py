import sys
from collections import defaultdict

input = sys.stdin.readline

N, L, R = map(int, input().split())

def find_root(cur):
    while cur != group[cur[0]][cur[1]]:
        cur = group[cur[0]][cur[1]]
    return tuple(cur)

border = []
group = []
new_border = defaultdict(list)
delta = [[0, 1], [1, 0]]

for i in range(N):
    border.append(list(map(int, input().split())))
    group.append([(i,j) for j in range(N)])

print(group)

for i in range(N):
    for j in range(N):
        for dx, dy in delta:
            dx += i
            dy += j
            if 0 <= dx < N and 0 <= dy < N:
                if L <= abs(border[i][j] - border[dx][dy]) <= R:
                    group[dx][dy] = (i, j)
                    new_border[find_root((i, j))].append((dx, dy))

print(group)
print(new_border)

