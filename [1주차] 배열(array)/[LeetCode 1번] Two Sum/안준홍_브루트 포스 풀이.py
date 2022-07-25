class Solution(object):
    def twoSum(self, nums, target):
        # 이중 for문을 통해 두 수의 합을 구하여 target과 비교
        for idx1 in range(len(nums)):
            for idx2 in range(idx1+1, len(nums)):
                if nums[idx1] + nums[idx2] == target:
                    return [idx1, idx2]