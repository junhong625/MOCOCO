class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1_set = set(nums1)
        num2_set = set(nums2)
        
        return list(num1_set & num2_set)
    
    