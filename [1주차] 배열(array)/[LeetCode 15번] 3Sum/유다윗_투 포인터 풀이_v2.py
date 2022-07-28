class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums = sorted(nums)
        left = 0
        result = []

        # 기둥을 옮겨가는 for문
        for p in range(len(new_nums)):
            if p > 0 and new_nums[p-1] == new_nums[p]: # 이 if문을 추가하지 않으면 time limit에 걸림;; 신기방기
                continue
            left = p + 1
            right = len(new_nums) - 1
            if p == right:
                break

            # 투 포인터 움직이기
            while True:
                if left == right:
                    break
                if (new_nums[p] + new_nums[left] + new_nums[right]) == 0 and ([new_nums[p], new_nums[left], new_nums[right]] not in result):
                    result.append([new_nums[p], new_nums[left], new_nums[right]])
                elif (new_nums[p] + new_nums[left] + new_nums[right]) > 0:
                    right -= 1
                else:
                    left += 1

        return result