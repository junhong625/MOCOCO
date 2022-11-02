'''
8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
'''
from itertools import combinations

def synergy(team):
    score = 0
    for i in range(0, len(team)-1):
        for j in range(i, len(team)):
            score += arr[team[i]][team[j]] + arr[team[j]][team[i]]
    return score


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]


sl = [i for i in range(N)]
combi = list(combinations(sl, N//2))

minV = 9999
for i in combi:
    team1 = list(i)
    team2 = []
    for a in sl:
        if a not in team1:
            team2.append(a)
    temp = abs(synergy(team1) - synergy(team2))
    if temp < minV:
        minV = temp

print(minV)
