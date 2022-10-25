class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        cnt = 0
        while nums[0] !=  min(nums):
            nums = nums[1:] + [nums[0]]
            cnt += 1
        
        
        def bs(left, right):
            if left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    ans.append(pivot)
                    return
                
                elif nums[pivot] > target:
                    bs(left, pivot - 1)
                
                elif nums[pivot] < target:
                    bs(pivot + 1, right)
            
            else:
                ans.append(-1)
                return
        
        ans = []
        bs(0, len(nums) - 1)
        if ans[0] > -1:
            return (ans[0] + cnt) % len(nums)
        else:
            return -1