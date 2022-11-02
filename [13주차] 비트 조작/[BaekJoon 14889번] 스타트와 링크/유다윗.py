from itertools import combinations

def comb(arr):
    half = list(combinations(arr, N//2))
    for h in half:
        temp = arr[:]
        for i in h:
            temp.remove(i)
        teams.append([list(h), temp])


def get_score(arr):
    result = 0
    for (i, j) in arr:
        result += scores[i-1][j-1] + scores[j-1][i-1]
    return result


N = int(input())

scores = [list(map(int, input().split())) for _ in range(N)]
players = [i for i in range(1, N+1)]
teams = []
comb(players)
possible = len(list(combinations(players[:N//2], 2)))
min_value = 200 * possible
for t in teams:
    a_possible = list(combinations(t[0], 2))
    b_possible = list(combinations(t[1], 2))
    temp_min = get_score(a_possible)
    temp_min = abs(temp_min - get_score(b_possible))
    if temp_min < min_value:
        min_value = temp_min
print(min_value)



