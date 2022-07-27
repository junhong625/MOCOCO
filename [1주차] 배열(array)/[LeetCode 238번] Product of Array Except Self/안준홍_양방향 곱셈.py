class Solution(object):
    def productExceptSelf(self, nums):
        # 양방향의 곱셈이 곱해질 변수
        result = [1] * len(nums)
        
        left_mul = 1
        # 왼쪽 방향에서부터 현재 index의 값을 left_mul에 곱한 다음 index+1 값에 곱해주는 반복문
        for i in range(1, len(nums)):
            left_mul *= nums[i-1]
            result[i] *= left_mul

        # 오른쪽 방향에서부터 현재 -index의 값을 right_mul에 곱한 다음 -index-1 값에 곱해주는 반복문
        right_mul = 1
        for i in range(-2, -(len(nums))-1, -1):
            right_mul *= nums[i+1]
            result[i] *= right_mul
        
        return result