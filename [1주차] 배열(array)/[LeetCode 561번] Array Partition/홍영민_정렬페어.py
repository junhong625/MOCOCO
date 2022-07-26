def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()
    # 왼쪽에서 하나씩 쌍으로 묶어서 max화 시키기
    result = 0
    for i in range(0,len(nums),2):
        result += min(nums[i],nums[i+1])
    return result