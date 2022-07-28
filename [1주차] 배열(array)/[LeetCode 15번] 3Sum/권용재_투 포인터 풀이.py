class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        results = []
        nums.sort()                       
        for i in range(len(nums) - 2):
            #중복값 건너뛰기           
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left_idx = i+1
            right_idx = len(nums) - 1
            while left_idx < right_idx:
                sum = nums[i] + nums[left_idx] + nums[right_idx]
                if sum < 0:
                    left_idx += 1
                elif sum > 0:
                    right_idx -= 1
                else:
                    results.append([nums[i] , nums[left_idx] , nums[right_idx]])

                    while left_idx < right_idx and nums[left_idx] == nums[left_idx + 1]:
                        left_idx += 1
                    while left_idx < right_idx and nums[right_idx] == nums[right_idx - 1]:
                        right_idx -=1

                    left_idx += 1
                    right_idx -= 1

        return results
