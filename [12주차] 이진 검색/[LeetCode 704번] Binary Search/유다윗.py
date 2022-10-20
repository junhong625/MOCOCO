# 704. Binary Search
# 248ms / 15.5mb
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        success = False                         # 탐색 성공 여부 체크
        while left <= right:                    # left와 right가 교차하면 break
            middle = (left+right) // 2
            if nums[middle] == target:
                success = True                  # 탐색 성공
                break
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        if success:
            return middle
        return -1