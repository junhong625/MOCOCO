class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for unit in sorted(intervals):
            if ans and ans[-1][-1] >= unit[0]:
                if unit[-1] > ans[-1][-1]:
                    ans[-1][-1] = unit[-1]
            
            else:
                ans.append(unit)
        
        return ans
            