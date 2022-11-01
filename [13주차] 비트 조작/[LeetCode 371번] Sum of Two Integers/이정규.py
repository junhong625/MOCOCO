class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while b:
            sums = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sums
            b = carry
            #print('mask')
            #print(bin(mask))
            #print('sums')
            #print(a, bin(a))
            #print('carry')
            #print(b, bin(b))
        
        if a > 0x7fffffff:
            #print('~(a^mask)')
            #print(~(a^mask))
            return ~(a^mask)
        
        #print('ans')
        #print(a)
        return a

        # https://leetcode.com/problems/sum-of-two-integers/discuss/776952/python-best-leetcode-371-explanation-for-python