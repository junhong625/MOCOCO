# 78. Subsets

def subsets(nums):
    def dfs(cand):     
        result.append(combination[:])                       # 현재 조합을 result에 추가                    
        if len(combination) == len(nums):                   # 조합의 길이가 nums의 길이와 일치할 경우 dfs 종료
            return
        else:                                         
            for i in cand:
                if combination and i < combination[-1]:     # combination에 원소가 존재하고, 최근 추가된 원소가 i보다 클 경우 continue -> 중복 제거 역할
                    continue       
                combination.append(i)                       # 조합에 원소 추가
                next_cand = cand[:]                         
                next_cand.remove(i)                         # 현재 원소를 제외한 숫자 리스트 -> 다음 dfs의 input
                dfs(next_cand)
                combination.pop()


    result = []
    combination = []
    dfs(nums)
    return result


if __name__ == '__main__':
    print(subsets([1,2,3]))