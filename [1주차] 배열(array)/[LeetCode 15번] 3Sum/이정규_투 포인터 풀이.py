class Solution(object):
    def threeSum(self, nums):
        ans = []
        nums.sort()
        for i in range(len(nums)-2) :
            left = i + 1 # 투 포인터를 쓰기 위해, i 뒤의 배열 중 양끝 잡기
            right = len(nums) - 1
            

            if (nums[i] == nums[i - 1]) and i > 0 : # 중복된 수열 정리
                continue
            
            while left < right :
                if nums[i] + nums[left] + nums[right] > 0 : # 투 포인터 이동
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0 :
                    left += 1
                else :
                    ans.append([nums[i], nums[left], nums[right]])        
                    while left < right and nums[right] == nums[right - 1] :
                        right -= 1 # 중복된 수열 정리
                    right -= 1
                    while left < right and nums[left] == nums[left + 1] :
                        left += 1 # 중복된 수열 정리
                    left += 1
        return (ans)