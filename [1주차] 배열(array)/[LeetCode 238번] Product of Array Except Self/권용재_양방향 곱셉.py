class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []
        p = 1
        for i in range(len(nums)):
            result.append(p)
            p *= nums[i]
            
        q = 1
        for i in range(len(nums)-1, 0 -1, -1):
            result[i] *= q
            q *= nums[i]
            
        return result




#다른사람 풀이 space = O(1)

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         ans = [1 for _ in nums]
        
#         left = 1
#         right = 1
        
#         for i in range(len(nums)):
#             ans[i] *= left
#             ans[-1-i] *= right
#             left *= nums[i]
#             right *= nums[-1-i]
        
#         return ans