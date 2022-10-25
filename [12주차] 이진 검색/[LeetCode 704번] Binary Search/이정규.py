class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def bs(left, right):
            if left <= right:
                pivot = (left + right) // 2
                
                if target < nums[pivot]:
                    return bs(left, pivot - 1)
                
                elif target > nums[pivot]:
                    return bs(pivot + 1, right)
                
                else:
                    return pivot
            else:
                return -1
        
        return bs(0, len(nums) - 1)