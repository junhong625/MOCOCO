class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for unit in nums:
            print('before')
            print(bin(ans))
            print(bin(unit))
            ans = ans^unit
            print('after')
            print(bin(ans))
            
        return ans