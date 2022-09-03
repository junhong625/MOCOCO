## 72ms(99.48%) 16.6bm(86.89%)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        
        count = Counter(nums) # Counter함수로 Counting sort처리
        count = sorted(count, key=lambda x:count[x], reverse=True) # key에 lambda를 사용하여 정렬, reverse를 사용하여 역순으로 정렬
        return count[:k] # k를 이용하여 범위 슬라이싱