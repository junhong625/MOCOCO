class Solution(object):
    def maxProfit(self, prices):
        to_the_moon = prices
        mu_rup, ik_jeol = 2147483647, 0
        
        for gazua in to_the_moon :
            mu_rup = min(mu_rup, gazua)
            ik_jeol = max(ik_jeol, gazua - mu_rup)
        
        return(ik_jeol)
