import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word = sorted([input().strip() for _ in range(n)])
prefix = sorted([input().strip() for _ in range(m)])


cnt, idx = 0, 0
for unit in prefix:
    for i in range(idx, n):
        if unit == word[i][:len(unit)]:
            cnt += 1
            idx = i
            break

print(cnt)