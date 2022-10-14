class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        li = sorted(points, key=lambda x: x[0]**2 + x[1]**2)
        print(li[:k])
        return li[:k]
    
    # 교재에서는 heap을 활용해서 distance 계산 이후 횟수 만큼 pop을 진행