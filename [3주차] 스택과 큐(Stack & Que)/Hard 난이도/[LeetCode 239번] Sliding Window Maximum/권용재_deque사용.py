from collections import deque
class Solution(object):
    def maxSlidingWindow(self,nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    

        if k == 0:
            return []

        d = deque()
        result = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)

            if d[0] == i-k:
                d.popleft()

            if i >= k-1:
                result.append(nums[d[0]])

        return result
