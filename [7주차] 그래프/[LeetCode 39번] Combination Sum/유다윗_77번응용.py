# 39_combination Sum

def combinationSum(candidates, target):
    def dfs(nums, start=0):                         
        if sum(combination) == target:                # 조합의 합이 target과 일치할 경우 result에 추가하고 dfs 종료
            result.append(combination[:])
            return
        elif sum(combination) > target:               # 조합의 합이 target을 넘어갈 경우 dfs 종료
            return
        else:                                         # 조합의 합이 target보다 작을 경우,
            for i in range(start, len(nums)):         # start: 가장 최근 조합에 추가된 원소의 인덱스 -> 중복 조합 가능
                combination.append(nums[i])
                dfs(nums, i)
                combination.pop()


    result = []
    combination = []
    dfs(candidates)
    return result


if __name__ == '__main__':
    print(combinationSum([2,3,6,7], 7))