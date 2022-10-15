# 75. Sort Colors
# 44ms / 13.8mb

# flow
# 1. 0은 앞으로, 2는 뒤로 옮긴다.


def sortColors(nums) -> None:
        N = len(nums)
        idx = 0
        count_2 = 0                     # 2를 뒤로 보낸 횟수
        while idx < N:
            if nums[idx] == 0:          # 0이 나올 경우 맨 앞으로 옮기기
                nums.pop(idx)
                nums.insert(0, 0)
                if not nums[idx]:       # 또 다시 0이 idx에 위치하면 idx 옮기기
                    idx += 1
                
            elif nums[idx] == 2:        # 2가 나올 경우 맨 뒤로 옮기기
                if N-idx == count_2:    # 2를 뒤로 보낸 횟수와 남은 원소 개수가 일치할 경우 break
                    break
                nums.pop(idx)    
                nums.insert(N, 2)
                count_2 += 1

            else:                       # 1인 경우
                idx += 1
            
            
if __name__ == '__main__':
    sortColors([1,0,0])
    
