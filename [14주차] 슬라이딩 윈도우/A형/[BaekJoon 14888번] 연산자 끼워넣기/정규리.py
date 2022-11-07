import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
yeonsan = list(map(int, input().split()))

min_res = 1000000000
max_res = -1000000000
def sachik(i, ys, stack):
    print(i, ys, stack)
    if i == N:
        print('res')
        print(i, ys, stack)
        global min_res, max_res
        if stack < min_res:
            min_res = stack
        if stack > max_res:
            max_res = stack
    
    
    if ys[0]:
        if -1000000000 <= stack + nums[i] <= 1000000000:
            ys[0] -= 1
            sachik(i + 1, ys[:], stack + nums[i])
            ys[0] += 1
    
    if ys[1]:
        if -1000000000 <= stack - nums[i] <= 1000000000:
            ys[1] -= 1
            sachik(i + 1, ys[:], stack - nums[i])
            ys[1] += 1

    if ys[2]:
        if -1000000000 <= stack * nums[i] <= 1000000000:
            ys[2] -= 1
            sachik(i + 1, ys[:], stack * nums[i])
            ys[2] += 1
    
    if ys[3]:
        if -1000000000 <= stack // nums[i] <= 1000000000:
            ys[3] -= 1
            if stack > 0:
                sachik(i + 1, ys[:], stack // nums[i])
            else:
                sachik(i + 1, ys[:], -(-stack // nums[i]))
            ys[3] += 1

sachik(1, yeonsan[:], nums[0])
print(max_res)
print(min_res)