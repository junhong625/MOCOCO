class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # xor연산을 통해 비트 거리 비교
        result = bin(x ^ y)
        return sum(map(int,result[2:]))