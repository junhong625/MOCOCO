def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    result = []
    for idx, i in enumerate(nums[:-1]):
            left = idx+1
            right = len(nums)-1
            while left < right :
                sum_num = i + nums[left] + nums[right]
                if sum_num >0:
                    left += 1
                elif sum_num <0:
                    right -= 1
                else:
                    result.append([i,nums[left],nums[right]])
                    right -= 1
                    left += 1
    return result
    ##틀렸음. 왜 안되는지는 내일...
    