# 167. Two Sum II - Input Array Is Sorted
# 363ms / 14.9mb

# flow
# 1. 왼쪽에서 오른쪽으로 움직이는 포인터(left) 생성
# 2. (target-left 원소) 값을 left의 다음 인덱스 원소부터 마지막 원소 사이에서 찾는다.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        N = len(numbers)
        left = 0                                        # left 포인터 초기화
        
        while True:                                     # left 포인터 옮겨가며 이진탐색
            now_search = target - numbers[left]         # 이진탐색 시 target이 되는 값

            b_left = left + 1                           # 이진탐색의 왼쪽 포인터 초기화
            b_right = N - 1                             # 이진탐색의 오른쪽 포인터 초기화
            while b_left <= b_right:
                middle = (b_left + b_right) // 2
                if numbers[middle] == now_search:
                    return [left+1, middle+1]
                elif numbers[middle] > now_search:
                    b_right = middle - 1
                else:
                    b_left = middle + 1
            left += 1                                   # 탐색 실패 시 left 옮겨주고 다시 순회