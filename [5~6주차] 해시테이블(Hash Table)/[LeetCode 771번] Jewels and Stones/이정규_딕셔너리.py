class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        list_chk = []               # 보석 추가
        for unit in jewels:
            list_chk.append(unit)
        
        cnt = 0
        for chk in stones:          # 보석 카운트
            if chk in list_chk:
                cnt += 1
            
        return cnt