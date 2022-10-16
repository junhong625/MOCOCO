class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def swap(a, b):
            return str(a) + str(b) < str(b) + str(a)
    
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if swap(nums[j - 1], nums[j]):
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        
        return str(int(''.join(map(str, nums))))