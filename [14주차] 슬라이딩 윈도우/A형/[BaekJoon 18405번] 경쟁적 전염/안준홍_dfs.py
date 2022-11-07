import sys

input = sys.stdin.readline

def dfs(idx, total):
    if idx == len(nums):    # 종료기준
        # print(total)
        sit.append(total)   # 경우의 수 모두 sit에 추가
        return

    for i in range(4):      # 연산자의 개수에 맞춰 dfs 실행
        if operators[i]:    # 연산자가 존재할 경우에만 다음 조건 실행
            if i == 0:
                operators[i] -= 1
                dfs(idx+1, total+nums[idx])
                operators[i] += 1
            elif i == 1:
                operators[i] -= 1
                dfs(idx+1, total-nums[idx])
                operators[i] += 1
            elif i == 2:
                operators[i] -= 1
                dfs(idx+1, total*nums[idx])
                operators[i] += 1
            else:
                operators[i] -= 1
                dfs(idx+1, int(total/nums[idx]))
                operators[i] += 1

N = int(input())

nums = list(map(int, input().split()))
operators = list(map(int,input().split()))
sit = []

dfs(1, nums[0])

print(max(sit))             # 나올 수 있는 경우의 수들 중 가장 큰 값 출력
print(min(sit))             # 나올 수 있는 경우의 수들 중 가장 작은 값 출력