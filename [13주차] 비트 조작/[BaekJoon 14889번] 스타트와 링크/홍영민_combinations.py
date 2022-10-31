# A팀과 B팀으로 구성 / 각 팀 수치 계산 및 비교 / 최소값 갱신
from itertools import combinations

n = int(input())
power = [ list(map(int, input().split())) for _ in range(n)]

# print(n)
# print(power)
members = [i for i in range(n)]
member_option = list(combinations(members, n//2))
base = set(members)
result = 100*n
for option in member_option:
    A = list(option)
    B = list(base-set(option))
    ascore = 0
    bscore = 0
    for i in range(0,n//2-1):
        for j in range(i+1,n//2):
            ascore += power[A[i]][A[j]]
            ascore += power[A[j]][A[i]]
            bscore += power[B[i]][B[j]]
            bscore += power[B[j]][B[i]]
    fight = abs(ascore - bscore)
    if result > fight:
        result = fight
print(result)
