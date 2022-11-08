# 14888
# 33908kb / 216ms

def calculator(a, b, num):                                      # 연산자별 계산 결과를 반환하는 함수
    if num == 0:
        return a + b
    elif num == 1:
        return a - b
    elif num == 2:
        return a * b
    else:
        if a < 0 and b > 0:
            return -(-a // b)
        else:
            return a // b

def make_perms(perm, perm_idx, operators):                      # 연산자 순열을 구하는 함수
    if perm_idx == N-1:                                         # 순열을 구하면 operators_perms에 넣기
        operators_perms.append(perm[:])
    else:
        for i in range(4):
            if operators[i]:
                operators[i] -= 1                               # 사용한 연산자 -1
                perm[perm_idx] = i                              # 현재 인덱스에 해당 연산자 넣기
                make_perms(perm, perm_idx+1, operators)
                operators[i] += 1
                perm[perm_idx] = 0


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

operators_perms = []                                            # 모든 연산자 배치 순열을 넣을 리스트

perm = [0] * (N-1)                                              # 순열 리스트 초기화
make_perms(perm, 0, operators)                                  # 모든 순열 구하기

max_result = -1e9 - 1
min_result = 1e9 + 1
for op_perm in operators_perms:                                 # 순열 하나씩 꺼내기
    result = nums[0]                                            # 연산 결과인 result를 nums의 첫 번째 값으로 초기화
    for n in nums[1:]:
        op = op_perm.pop(0)                                     # 연산자 꺼내기
        result = calculator(result, n, op)                      # calculator 함수 사용하여 연산 진행
    if result > max_result:
        max_result = result
    if result < min_result:
        min_result = result
print(max_result, min_result)
