class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # total = 0
        # for j in jewels:
        #     total += stones.count(j)
        # return total
        jewel_cnt = {}
        for s in stones:
            if s in jewels:
                if s in jewel_cnt:
                    jewel_cnt[s] += 1
                else:
                    jewel_cnt[s] = 1
        
        return sum(jewel_cnt.values())