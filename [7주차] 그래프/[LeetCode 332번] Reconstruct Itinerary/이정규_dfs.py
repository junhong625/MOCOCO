class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        def dfs(s, d):
            while s in dic_t and dic_t[s]:
                dfs(dic_t[s].pop(0), d)
            d.append(s)        
        
        stack = []
        dic_t = {}
        
        for unit in sorted(tickets):
            if unit[0] not in dic_t:
                dic_t[str(unit[0])] = [str(unit[1])]
            else:
                dic_t[str(unit[0])].append(str(unit[1]))
        
        dfs('JFK', stack)
        
        return stack[::-1] # 140ms / 13.8mb