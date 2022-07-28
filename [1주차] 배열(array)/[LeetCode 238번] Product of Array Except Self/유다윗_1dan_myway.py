
## 의문: if문과 for문이 많다고 느꼈는데도 굉장히 빠른 속도를 기록함...왜?...(Runtime: 235 ms, faster than 95.54%...)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 0이 두 개 이상이면 원소가 모두 0
        if nums.count(0) >= 2:
            return [0] * len(nums)

        # 0이 한 개일 경우
        elif nums.count(0) == 1:
            mulpiple = 1
            for i in nums:
                if i == 0:
                    continue
                mulpiple *= i
            result = [0] * len(nums)
            zero_idx = nums.index(0)
            result[zero_idx] = int(mulpiple)
            return result
        # 0이 없는 경우
        else:
            mulpiple = 1
            result = []
            for i in nums:
                mulpiple *= i
            for i in nums:
                result.append(int(mulpiple/i))
            return result