class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        left = 0
        right = 1
        
        max_profit = 0
        
        while right < len(prices):
            max_now = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(max_profit, max_now)
            else:
                left = right
            right +=1        
        return max_profit




# 다른사람 풀이
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         buy = prices[0]     #Left pointer
#         sell = prices[0]    #Right Pointer
        
#         maxProfit = 0
        
#         for element in prices[1:]:
#             if (element < buy):
#                 buy, sell = element, element
#             elif (element > sell):
#                 sell = element
#                 maxProfit = max(maxProfit, sell - buy)
#         return maxProfit
    
#         if (len(prices) < 2):
#             return 0