class Solution(object):
    def threeSum(self, nums):
    # 투 포인터로 풀기 위해 정렬
        nums.sort()
        result = []
        # 첫번째 값이 될 기준을 정해주는 for문 
        for i in range(len(nums)-2):
            # i의 값이 다음과 중복될 경우 continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # left에는 i 다음 기준으로 제일 왼쪽 인덱스, right에는 nums의 마지막 인덱스
            left, right= i+1, len(nums)-1

            while left < right:
                # 1번째, 2번째, 3번째 수의 합
                sums = nums[i] + nums[left] + nums[right]
                # 0보다 작을 경우 right의 값을 -1을 통해 좀 더 작은 수로 이동
                if sums > 0:
                    right -= 1
                # 0보다 클 경우 left의 값을 +1을 통해 좀 더 큰 수로 이동
                elif sums < 0:
                    left += 1
                # 0과 같을 경우 모든 수를 list형태로 result에 추가
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # 중복되는 경우를 넘어가기 위한 while문
                    while left < right and nums[left] == nums[left + 1]: 
                        left += 1 
                    # 중복되는 경우를 넘어가기 위한 while문
                    while left < right and nums[right] == nums[right - 1]: 
                        right -= 1 
                    left += 1 
                    right -= 1
        return result