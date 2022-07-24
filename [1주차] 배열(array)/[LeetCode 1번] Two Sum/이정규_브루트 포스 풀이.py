class Solution(object):
    def twoSum(self, nums, target):
        ans = [0] * 2
        for i in range(len(nums)) :
            for j in range(i + 1, len(nums)) :
                if nums[i] + nums[j] == target :
                    ans[0] = i
                    ans[1] = j 
        return (ans)