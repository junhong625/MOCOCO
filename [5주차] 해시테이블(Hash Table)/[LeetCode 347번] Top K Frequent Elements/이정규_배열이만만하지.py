class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for unit in nums:                               # 딕녀서리에 정리
            if d and unit in d:
                d[unit] += 1
            else:
                d[unit] = 1
        
        res = []
        for unit in d:
            res.append([d[unit], unit])                 # 등장횟수를 앞세워 배열화
            
        ans = []
        for unit in sorted(res, reverse = True)[:k]:    # k순위까지 뽑아서
            ans.append(unit[1])
        
        
        return ans                                      # 리턴