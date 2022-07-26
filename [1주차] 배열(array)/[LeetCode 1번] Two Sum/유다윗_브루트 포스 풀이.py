class Solution(object):
    def twoSum(self, nums, target):
        for idx, i in enumerate(nums):
            for idx2, j in enumerate(nums[idx+1:]):
                if i + j == target:
                    return [idx, idx2+idx+1]