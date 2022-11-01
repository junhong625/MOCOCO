import sys
input = sys.stdin.readline

N = int(input())
startlink = [list(map(int, input().split())) for _ in range(N)]

def makecombi(i, stack, set_l):
    if len(stack) == N // 2:
        set_l.add(tuple(stack))
        return
        
    if i < N :
        makecombi(i + 1, stack, set_l)
        makecombi(i + 1, stack + [i], set_l)

start = set()
makecombi(1, [], start)

min_cha = 100 * (N//2)
for unit in list(start):
    link = []
    for x in range(1, N + 1):
        if x not in unit:
            link.append(x)

    sum_s = 0
    sum_l = 0
    for y in unit:
        for x in unit:
            if y == x:
                continue
            else:
                sum_s += startlink[y - 1][x - 1]
    
    for y in link:
        for x in link:
            if y == x:
                continue
            else:
                sum_l += startlink[y - 1][x - 1]

    if abs(sum_l - sum_s) < min_cha:
        min_cha = abs(sum_l - sum_s)

print(min_cha)