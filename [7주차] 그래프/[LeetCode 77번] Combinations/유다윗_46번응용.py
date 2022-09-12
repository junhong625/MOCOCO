# 77_combinations

def combine(n: int, k: int):

    def dfs(nums, start=1):
        if len(combination) == k:                 # 조합이 k개일 때 result에 조합 추가하고 함수 종료
            result.append(combination[:])
            return
        
        else:
            for i in range(start, n+1):           # start부터 마지막 수까지 순회
                next_cand = nums[:]             
                next_cand.remove(i)               # 조합에 추가되는 값을 제외한 수의 리스트 -> dfs의 인자로 넣음

                combination.append(i)             # 조합에 추가되는 값을 combination에 넣기
                start = combination[-1]+1         # 조합에 추가되는 값에 +1을 한 값을 start로 지정
                dfs(next_cand, start)           
                combination.pop()                 # 다음 순회값을 받기 위해 pop


    result = []
    combination = []
    nums = [i for i in range(1, n+1)]
    dfs(nums)
    return result


if __name__ == '__main__':
    print(combine(3, 2))