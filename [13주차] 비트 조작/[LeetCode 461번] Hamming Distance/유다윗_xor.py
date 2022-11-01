# 461. Hamming Distance
# 39ms / 13.8mb

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = bin(x ^ y)
        return xor.count('1')