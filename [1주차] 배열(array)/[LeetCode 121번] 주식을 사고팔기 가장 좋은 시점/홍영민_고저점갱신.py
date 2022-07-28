class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## 저점과 고점을 리스트 안에서 계속 갱신
        low = 0
        profit = 0
        for idx, i  in enumerate(prices):
            if idx == 0: # 첫값은 저점으로 설정
                low = i
                continue
            if low >= i:
                low = i
                continue
            else :
                profit_new = i - low # 수익의 고점 비교
                if profit < profit_new:
                    profit = profit_new
        return profit
                
            