class Solution(object):
    def productExceptSelf(self, nums):
        ans = []
        res = 1

        for i in range(len(nums)) :
            ans.append(res)
            res = res * nums[i]
        
        res = 1
        for j in range(len(nums) - 1, - 1, -1) :
            ans[j] = res * ans[j]
            res = res * nums[j]
            
        return (ans)