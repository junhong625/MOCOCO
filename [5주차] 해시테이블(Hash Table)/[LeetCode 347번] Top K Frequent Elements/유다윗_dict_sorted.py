
def topKFrequent(nums, k):
    ## 1. nums 각 원소에 10000씩 더해주기
    nums = list(map(lambda x:x+10000, nums))


    ## 2. 카운팅 배열 만들기 ##
    counts = [0] * 20001            # -1부터 -10000까지 1만개, 1부터 10000까지 1만개, 0
    keys = list(set(nums))          # unique 원소들
    
    for i in nums:
        counts[i] += 1
    

    ## 3. 딕셔너리 만들기 ##
    nums_dict = {}
    for key in keys:
        nums_dict[key] = counts[key]

    
    ## 4. 원소 개수 기준 내림차순 정렬 리스트 만들기 ##
    nums_dict = dict(sorted(nums_dict.items(), key=lambda x:x[1], reverse=True))
    elements_sorted = list(nums_dict.keys())


    ## 5. 출력하기
    return list(map(lambda x:x-10000, elements_sorted[:k]))


if __name__ == '__main__':
    print(topKFrequent([4,1,-1,2,-1,2,3], 2))