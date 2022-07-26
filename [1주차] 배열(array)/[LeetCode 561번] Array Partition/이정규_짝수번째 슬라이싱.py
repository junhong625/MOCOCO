class Solution(object):
    def arrayPairSum(self, nums):
        total = 0
        nums.sort() # 크기순 정렬
        total = sum(nums[::2])
        # min에 큰 수가 들어오려면 맞닿은 큰 수부터 짝을 지어야 하므로, 
        # 결국 홀수번째 숫자가 min이 될 수밖에 없는 구조이다.
        # 따라서 2개씩 슬라이싱해서 취합.
        return (total)