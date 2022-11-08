# 239. Sliding Window Maximum

# 46 / 51
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        right = left + k - 1
        result = [0] * (len(nums) - k + 1)
        result_top = -1
        while right < len(nums):
            now_nums = nums[left:right+1]
            max_num = (max(now_nums))
            max_num_idx = now_nums.index(max_num)
            
            while max_num_idx > -1 and right < len(nums) and nums[right] <= max_num:
                max_num_idx -= 1
                result_top += 1
                result[result_top] = max_num
                right += 1
            left = right - k + 1
        return result