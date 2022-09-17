# 77_combinations

def combine(n: int, k: int):

    def dfs(start=1):
        if len(combination) == k:                 # 조합이 k개일 때 result에 조합 추가하고 함수 종료
            result.append(combination)
            return
        
        else:
            for i in range(start, n+1):           # start부터 마지막 수까지 순회
                combination.append(i)             # 조합에 추가되는 값을 combination에 넣기
                dfs(combination[-1]+1)            # 조합에 추가되는 값에 +1을 한 값을 start로 지정
                combination.pop()                 # 다음 순회값을 받기 위해 pop


    result = []
    combination = []
    dfs()
    return result


if __name__ == '__main__':
    print(combine(3, 2))