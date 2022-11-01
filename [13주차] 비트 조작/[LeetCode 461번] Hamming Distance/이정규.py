class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = bin(x^y)
        cnt = 0
        for unit in str(ans)[2:]:
            if int(unit):
                cnt += 1
                
        return cnt