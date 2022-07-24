class Solution(object):
    def twoSum(self, nums, target):
        for idx1 in range(len(nums)):
            for idx2 in range(idx1+1, len(nums)):
                if nums[idx1] + nums[idx2] == target:
                    return [idx1, idx2]