# 191. Number of 1 Bits
# 59ms / 13.8mb


class Solution:
    def hammingWeight(self, n: int) -> int:
        count_1 = 0
        for i in range(len(bin(n))-2):
            if n & (1 << i):
                count_1 += 1
        return count_1
