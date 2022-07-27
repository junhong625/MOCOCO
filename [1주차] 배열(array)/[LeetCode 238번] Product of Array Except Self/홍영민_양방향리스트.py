class Solution(object):
    def productExceptSelf(self, nums):

        result = []
        #앞으로 곱하기 * 뒤로 곱하기 = 앞뒤 곱
        #앞으로 곱하기 = 0,1,12,123,1234
        #뒤로 곱하기 = 0,5,54,543,5432
        # 각 결과 1: 2345(0*5432) 2: 1345(1*543) 3: 1245 (12*54) 4 : 1235(123*5) 5 : 1234 (0*1234)
        forward = []
        short = 1
        long = len(nums)
        for i in range(long):
            forward.append(short)
            short *= nums[i]
        backward = []
        short = 1
        for j in range(long-1,-1,-1):
            backward.append(short)
            short*=nums[j]
        for k in range(long):
            multi = forward[k] * backward[long-1-k]
            result.append(multi)
        return result
