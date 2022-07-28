
### 후우 타임아웃...###

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        new_nums = sorted(nums)
        left = 0
        result = []

        # left를 옮겨가는 while문
        while True:
            right = len(nums) - 1
            if (left == right) or (new_nums[left] >= 1):
                break

            # right를 옮겨가는 while문
            while True:
                if left == right:
                    break

                # middle을 옮겨가는 for문
                for i in range(right-1, left, -1):
                    triple = [new_nums[left], new_nums[right], new_nums[i]]
                    total = sum(triple)
                    if total < 0:
                        break
                    if (total == 0) and (triple not in result):
                        result.append(triple)

                right -= 1
            left += 1
        return result