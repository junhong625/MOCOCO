class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        for y, x in points:
            res.append([y**2 + x**2, y, x])
        
        res.sort()
        ans = []
        for i in range(k):
            ans.append(res[i][1:])
        
        return ans