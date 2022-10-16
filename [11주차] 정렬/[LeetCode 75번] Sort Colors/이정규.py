class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = [0] * 3
        for unit in nums:
            temp[unit] += 1
        
        idx = 0
        for i in range(3):
            for _ in range(temp[i]):
                nums[idx] = i
                idx += 1