class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        # xor연산을 진행하면 동일한 숫자에 대해서 결과값이 0이 나오게 된다
        # 0과 하나의 숫자는 하나의 숫자가 출력된다
        # 참고로 xor연산은 교환법칙이 성립한다
        return result