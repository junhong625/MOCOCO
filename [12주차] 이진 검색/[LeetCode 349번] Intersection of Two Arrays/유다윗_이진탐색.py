# 349. Intersection of Two Arrays
# 60ms / 14.1mb

# flow
# 1. 두 리스트 정렬 및 중복값 제거
# 2. 원소가 더 많은 리스트의 원소들을 target으로 이진탐색


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(arr, targets):
            N = len(arr) - 1
            result = []
            base_left = 0                                       # target을 순회할 때마다 left를 세팅해주는 변수

            for target in targets:
                left = base_left
                right = N
                while left <= right:                            # left와 right가 교차하면 break
                    middle = (left+right) // 2
                    if arr[middle] == target:
                        result.append(arr[middle])
                        base_left = middle + 1                  # 탐색에 성공하면 다음 순회 시 시작 left는 middle+1
                        break
                    elif arr[middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1
            return result
        
        
        nums1 = sorted(list(set(nums1)))                        # 중복 제거 및 정렬
        nums2 = sorted(list(set(nums2)))                        # 중복 제거 및 정렬
        
        if len(nums1) >= len(nums2):                            # 원소 개수가 더 많은 리스트가 targets 인자 값
            return binary_search(nums2, nums1)
        return binary_search(nums1, nums2)
