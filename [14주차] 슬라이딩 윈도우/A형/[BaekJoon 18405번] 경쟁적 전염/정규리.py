import sys, collections
input = sys.stdin.readline

N, K = map(int, input().split())
germs = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())


germ = []
for y in range(N):
    for x in range(N):
        if germs[y][x]:
            germ.append([y, x, germs[y][x], 0])

germ.sort(key= lambda x: (x[2]))
germ = collections.deque(germ)
while germ:
    #print(germ)
    y, x, val, time = germ.popleft()
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        sy = y + dy
        sx = x + dx
        if 0 <= sy < N and 0 <= sx < N:
            if germs[sy][sx] == 0 and time < S:
                germ.append([sy, sx, val, time + 1])
                germs[sy][sx] = val

#print(germs)
print(germs[X - 1][Y - 1])