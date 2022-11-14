class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        hold = prices[0]
        for i in prices:
            if i >= hold:
                result += i-hold
                hold = i
            else:
                hold = i
        return result