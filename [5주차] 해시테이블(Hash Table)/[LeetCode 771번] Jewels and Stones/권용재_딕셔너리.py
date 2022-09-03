class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        #키값만큼 새로 dictionary 생성
        Map = dict()
        for i in jewels:
            Map[i] = Map.get(i,0)
        
        # 키값이 stone에 있으면 value +1
        for i in stones:
            if i in Map:
                Map[i] = Map.get(i,0) + 1 
        return sum(Map.values())