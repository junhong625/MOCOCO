# 33. Search in Rotated Sorted Array
# 77ms / 14.3mb

# flow
# 1. pivot을 찾는다.
# 2. 첫 번째 인덱스와 target을 비교해서
# target이 더 크면 left=0, right=pivot-1
# target이 더 작으면 left=pivot, right=len(nums)-1
# 3. 이진 탐색


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(arr, k, left, right):
            success = False                                 # 탐색 성공 여부 체크
            while left <= right:                            # left와 right가 교차하면 break
                middle = (left+right) // 2
                if arr[middle] == k:
                    success = True                          # 탐색 성공
                    break
                elif arr[middle] > k:
                    right = middle - 1
                else:
                    left = middle + 1
            
            if success:
                return middle
            return -1
        

        pivot = 1                                           
        N = len(nums)
        while pivot < N:
            if nums[pivot-1] > nums[pivot]:                 # pivot 인덱스가 가장 작은 값
                break
            pivot += 1
        
        left = 0
        right = len(nums) - 1
        if target >= nums[0]:
            right = pivot - 1
        else:
            left = pivot
        
        result = binary_search(nums, target, left, right)
        return result
