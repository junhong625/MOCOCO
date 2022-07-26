class Solution(object):
    def arrayPairSum(self, nums:list)->int:
        # 오름차순 정렬
        nums.sort()
        # min의 최대값이 들어갈 변수
        pair_max = 0
        # 가장 작은 수부터 숫자 2개씩 묶어 min()함수를 적용한 값을 pair_max에 더하는 반복문 
        for idx in range(0, len(nums), 2):
            pair_max += min(nums[idx:idx+2])
        return pair_max